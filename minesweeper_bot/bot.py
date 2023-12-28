import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.client.telegram import TelegramAPIServer
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from configrereader import config


async def main():
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )

# Creating DB engine for PostgreSQL
engine = create_async_engine(config.postgres_dsn, future=True, echo=False)

# Creating DB connections pool
db_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Creating bot and its dispatcher
bot = Bot(token=config.bot_token,
          parse_mode='HTML')
if config.custom_bot_api:
    bot.session.api = TelegramAPIServer.from_base(config.custom_bot_api,
                                                  is_local=True)

# Choosing FSM storage
if config.bot_fsm_storage == 'memory':
    dp = Dispatcher(storage=MemoryStorage())
else:
    dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))

# Allow interaction in private chats (not groups or channels) only
dp.message.filter(F.chat.type == 'private')

# Register middlwares