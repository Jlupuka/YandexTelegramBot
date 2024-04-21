from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, ExcursionButtons
from lexicon.ru.text_lexicon import ExcursionText

router: Router = Router()


@router.message(Command(commands=[MainCommands.excursion.name]))
async def command_excursion(message: Message) -> None:
    await message.answer(text=ExcursionText.startExcursion,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(1, 1),
                             buttons=(ExcursionButtons.wardrobe,),
                             back=MainCommands.start.name
                         ))
