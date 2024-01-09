from contextlib import suppress
from uuid import uuid4

from aiogram import Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from cbdata import (ClickCallbackFactory, IgnoreCallbackFactory,
                    NewGameCallbackFactory, SwitchFlagCallbackFactory,
                    SwitchModeCallbackFactory)
from db.requests import log_game
from keyboards.kb_minefield import make_keyboard_from_minefield
from keyboards.kb_newgame import make_replay_keyboard
from minesweeper.game import (all_flags_match_bombs, all_free_cells_are_open,
                              gather_open_cells, get_fake_newgame_data,
                              get_real_game_data, make_text_table,
                              untouched_cells_count)
from minesweeper.states import ClickMode, CellMask


router = Router()

@router.callback_query(NewGameCallbackFactory.filter())
async def callback_newgame(call: types.CallbackQuery, state: FSMContext, callback_data: NewGameCallbackFactory):
    size = callback_data.size
    bombs = callback_data.bombs
    game_id = str(uuid4())
    newgame_dict = {'game_id': game_id, 'game_data': get_fake_newgame_data(size, bombs)}
    await state.set_data(newgame_dict)

    text = f"You're currently playing <b>{size}x{size}</b> field, <b>{bombs}</b> bombs"
    kb = make_keyboard_from_minefield(newgame_dict['game_data']['cells'], game_id, ClickMode.CLICK)
    if callback_data.as_separate:
        await call.message.delete_reply_markup()
        await call.message.answer(text, reply_markup=kb)
    else:
        await call.message.edit_text(text, reply_markup=kb)
    await call.answer()
