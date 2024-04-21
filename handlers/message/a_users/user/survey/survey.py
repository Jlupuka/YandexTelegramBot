from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import SurveyText
from service.botSerivce.keyboard_resize import KeyboardResize
from states.states import FSMServey

router: Router = Router()


@router.message(StateFilter(FSMServey.get_city))
async def get_city_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMServey.get_weather)
    await message.answer(text=SurveyText.getWeather,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(1,),
                             back=MainCommands.start.name
                         ))


@router.message(StateFilter(FSMServey.get_weather))
async def get_weather_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    await message.answer(text=SurveyText.endSurvey,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             buttons=StartButtons,
                             sizes=await KeyboardResize.two_one(
                                 count_main_buttons=len(StartButtons),
                                 count_any_buttons=0),
                         ))
