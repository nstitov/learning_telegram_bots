from dataclasses import dataclass
from typing import Optional

from environs import Env


@dataclass
class TgBot:
    token: str
    admins_lst: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: Optional[str]=None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(
        token=env('BOT_TOKEN'),
        admins_lst=list(map(int, env.list('ADMIN_IDS')))))
