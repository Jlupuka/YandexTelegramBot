from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import SurveyText

router: Router = Router()


@router.message(Command(commands=[MainCommands.stop.name]))
async def stop_servey(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    await message.answer(text=SurveyText.stopSurvey,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(2, 1),
                             buttons=StartButtons,
                             back_page=MainCommands.start.name
                         )
                         )
