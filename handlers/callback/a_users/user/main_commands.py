from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import MessageText
from service.botSerivce.keyboard_resize import KeyboardResize

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == MainCommands.start.name))
async def command_start(callback: CallbackQuery, callback_data: UserCallbackFactory, state: FSMContext) -> None:
    await state.set_state(None)
    await callback.message.edit_text(text=MessageText.start,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         sizes=await KeyboardResize.two_one(
                                             count_main_buttons=len(StartButtons),
                                             count_any_buttons=0),
                                         buttons=StartButtons,
                                         back_page=callback_data.page
                                     ))
