from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import StartButtons, SkipSurvey, MainCommands
from lexicon.ru.text_lexicon import SurveyText
from states.states import FSMServey

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == StartButtons.survey.name))
async def callback_start_survey(callback: CallbackQuery, callback_data: UserCallbackFactory, state: FSMContext) -> None:
    await state.set_state(FSMServey.get_city)
    await callback.message.edit_text(text=SurveyText.getCity,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=SkipSurvey,
                                         sizes=(1, 1),
                                         back=callback_data.back_page
                                     ))


@router.callback_query(UserCallbackFactory.filter(F.page == SkipSurvey.skip_get_city.name),
                       StateFilter(FSMServey.get_city))
async def get_weather_handler(callback: CallbackQuery, state: FSMContext) -> None:
    await state.set_state(FSMServey.get_weather)
    await callback.message.edit_text(text=SurveyText.getWeather,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         sizes=(1,),
                                         back=MainCommands.start.name
                                     ))
