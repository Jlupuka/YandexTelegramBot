from aiogram.types import Message, CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, TimerButtons, StartButtons
from lexicon.ru.text_lexicon import CommandText


async def sending_a_timer_message(message: Message, sleep_time: float) -> None:
    await message.answer(text=CommandText.completedTimer.format(sleepTime=sleep_time),
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(1,),
                             back=StartButtons.timer.name,
                             back_page=MainCommands.start.name
                         ))


async def sending_a_timer_callback(callback: CallbackQuery,
                                   callback_data: UserCallbackFactory) -> None:
    await callback.message.answer(
        text=CommandText.completedTimer.format(sleepTime=getattr(TimerButtons, callback_data.page).value),
        reply_markup=await Factories.factory_menu(
            callback_factory=UserCallbackFactory,
            sizes=(1,),
            back=callback_data.back_page,
            back_page=MainCommands.start.name
        ))
