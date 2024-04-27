import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot.commands import set_commands
from bot.configrereader import config
from bot.db.base import Base
from bot.handlers import callbacks, default_commands, statistics
from bot.middlewares.check_active_game import CheckActiveGameMiddleware
from bot.middlewares.db import DbSessionMiddleware


async def main():
    # Logging to stdout
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Creating DB engine for PostgreSQL
    engine = create_async_engine(config.postgres_dsn, future=True, echo=False)

    # Creating DB connections pool
    db_pool = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Creating bot and its dispatcher
    bot = Bot(token=config.bot_token, parse_mode="HTML")

    # Choosing FSM storage
    if config.bot_fsm_storage == "memory":
        dp = Dispatcher(storage=MemoryStorage())
    else:
        dp = Dispatcher(storage=RedisStorage.from_url(config.redis_dsn))

    # Allow interaction in private chats (not groups or channels) only
    dp.message.filter(F.chat.type == "private")

    # Register middlwares
    dp.message.middleware(DbSessionMiddleware(db_pool))
    dp.callback_query.middleware(CheckActiveGameMiddleware())
    dp.callback_query.middleware(DbSessionMiddleware(db_pool))

    dp.include_router(default_commands.router)
    dp.include_router(statistics.router)
    dp.include_router(callbacks.router)

    # Register /-commands in UI
    await set_commands(bot)

    try:
        print("Bot started.")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
    print("Bot finised.")
