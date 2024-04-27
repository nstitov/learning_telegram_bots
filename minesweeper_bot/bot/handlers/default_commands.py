from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

from bot.keyboards.kb_newgame import make_newgame_keyboard

router = Router()


@router.callback_query(F.data == "choose_newgame")
async def show_newgame_cb(call: CallbackQuery):
    await call.message.answer(
        "Press a button below to start a new game (previous one will be dismessed)\n"
        "Note: 6x6 and 7x7 fields look best on bigger screens or Desktop apps.",
        reply_markup=make_newgame_keyboard(),
    )
    await call.message.delete_reply_markup()
    await call.answer()


@router.message(Command("start"))
async def show_newgame_msg(message: Message):
    await message.answer(
        "Press a button below to start a new game (previous one will be dismissed)\n"
        "Note: 6×6 and 7×7 fields look best on bigger screens or Desktop apps.\n\n"
        "Press /help if you're unsure how to play Bombsweeper.",
        reply_markup=make_newgame_keyboard(),
    )


@router.message(Command("help"))
async def process_help_command(message: Message):
    await message.answer(
        "A quick guide how to play Bombsweeper is available here: "
        "https://telegra.ph/bombsweeper-how-to-play-09-08"
    )
