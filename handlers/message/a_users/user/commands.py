from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from lexicon.ru.lexicon import CommandText

from service.scriptsService.reformat_time import TimeService

router: Router = Router()


@router.message(Command("time"))
async def command_time(message: Message) -> None:
    await message.answer(text=CommandText.nowTime.format(nowTime=await TimeService.now_time()))


@router.message(Command("date"))
async def command_date(message: Message) -> None:
    await message.answer(text=CommandText.nowDate.format(nowDate=await TimeService.now_date()))
