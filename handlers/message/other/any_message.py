from aiogram import Router
from aiogram.types import Message

from lexicon.ru.lexicon import AnyMessage

router: Router = Router()


@router.message()
async def any_message(message: Message) -> None:
    await message.answer(text=AnyMessage.anyMessage.format(userMessage=message.text))
