from aiogram import Router
from aiogram.types import Message

from lexicon.ru.lexicon import RuMessage

router: Router = Router()


@router.message()
async def any_message(message: Message) -> None:
    await message.answer(text=RuMessage.anyMessage.format(userMessage=message.text))
