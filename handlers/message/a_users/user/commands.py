import asyncio
import re
from re import Match

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject

from lexicon.ru.lexicon import CommandText, ErrorText

from service.scriptsService.reformat_time import TimeService

router: Router = Router()


@router.message(Command(commands=["time"]))
async def command_time(message: Message) -> None:
    await message.answer(text=CommandText.nowTime.format(nowTime=await TimeService.now_time()))


@router.message(Command(commands=["date"]))
async def command_date(message: Message) -> None:
    await message.answer(text=CommandText.nowDate.format(nowDate=await TimeService.now_date()))


@router.message(Command(commands=["set_timer"]))
async def command_set_timer(message: Message, command: CommandObject) -> Message:
    if command.args and re.match(r"^-?\d*\.?\d+$", command.args):
        if 0 < (sleep_time := float(command.args)) < 1000:
            await asyncio.sleep(sleep_time)
            return await message.answer(text=CommandText.setTimer.format(sleepTime=sleep_time))
        return await message.answer(text=ErrorText.rangeTimer)
    return await message.answer(text=ErrorText.typeTimer)
