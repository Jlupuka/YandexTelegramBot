from dataclasses import dataclass
from typing import Union

from environs import Env


@dataclass
class Telegram:
    BotToken: str


@dataclass
class Config:
    Telegram: Telegram


def load_config(path: Union[str, None] = None) -> Config:
    env = Env()
    env.read_env(path=path)
    return Config(Telegram=Telegram(BotToken=env("BOT_TOKEN")))
