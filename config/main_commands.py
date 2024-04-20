from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.ru.lexicon import MainCommands
from service.loggerSerice.settings_logger import logger


async def load_main_commands(bot: Bot) -> None:
    commands: list[BotCommand] = [
        BotCommand(command=command_enum.name, description=command_enum.value)
        for command_enum in MainCommands
    ]
    await bot.set_my_commands(commands=commands)
    logger.debug("Uploaded the main commands!")
