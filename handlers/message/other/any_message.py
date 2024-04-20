from aiogram import Router
from aiogram.types import Message

from lexicon.ru.text_lexicon import MessageText

router: Router = Router()


@router.message()
async def any_message(message: Message) -> None:
    await message.answer(text=MessageText.anyMessage.format(userMessage=message.text))
