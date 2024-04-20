from aiogram import F, Router
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import MessageText

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == MainCommands.start.name))
async def command_start(callback: CallbackQuery, callback_data: UserCallbackFactory) -> None:
    await callback.message.edit_text(text=MessageText.start,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         sizes=(1, 1),
                                         buttons=StartButtons,
                                         back_page=callback_data.page
                                     ))
