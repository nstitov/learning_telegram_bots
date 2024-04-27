from aiogram.filters.callback_data import CallbackData

from bot.minesweeper.states import ClickMode


class NewGameCallbackFactory(CallbackData, prefix="newgame"):
    size: int
    bombs: int
    as_separate: bool


class ClickCallbackFactory(CallbackData, prefix="press"):
    game_id: str
    x: int
    y: int


class SwitchFlagCallbackFactory(CallbackData, prefix="flag"):
    game_id: str
    action: str
    x: int
    y: int


class SwitchModeCallbackFactory(CallbackData, prefix="switchmode_12"):
    game_id: str
    new_mod: int


class IgnoreCallbackFactory(CallbackData, prefix="ignore"):
    x: int
    y: int
