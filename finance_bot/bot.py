import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import config

logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
