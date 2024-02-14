import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import config
from keyboards.set_menu import set_main_menu
from lexicon.lexicon import translations

logger = logging.getLogger(__name__)


async def main():
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")

    dp = Dispatcher(storage=MemoryStorage(), _translations=translations)
    dp.message.filter(F.chat.type == "private")

    await set_main_menu(bot)

    await dp.start_polling(bot)


asyncio.run(main())
