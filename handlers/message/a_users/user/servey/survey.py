from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import MessageText
from states.states import FSMServey

router: Router = Router()


@router.message(StateFilter(FSMServey.get_city))
async def get_city_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMServey.get_weather)
    await message.answer(text=MessageText.get_weather,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(1,),
                             back=MainCommands.start.name
                         ))


@router.message(StateFilter(FSMServey.get_weather))
async def get_weather_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMServey.end_servey)
    await message.answer(text=MessageText.end_survey,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             buttons=StartButtons,
                             sizes=(2, 1),
                         ))
