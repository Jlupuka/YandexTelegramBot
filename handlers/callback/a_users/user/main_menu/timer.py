from typing import Union

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from detaTemplates.data_templates import DataTimer
from factory.factory import UserCallbackFactory
from handlers_scheduler.user.timer import sending_a_timer_callback
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import StartButtons, TimerButtons, MainCommands
from lexicon.ru.text_lexicon import MessageText, CommandText
from service.botSerivce.keyboard_resize import KeyboardResize
from service.scriptsService.time_service import TimeService

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == StartButtons.timer.name))
async def callback_timer(callback: CallbackQuery, callback_data: UserCallbackFactory) -> None:
    await callback.message.edit_text(text=MessageText.timer,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         sizes=(2, 1),
                                         buttons=TimerButtons,
                                         back_page=callback_data.page,
                                         back=MainCommands.start.name
                                     ))


@router.callback_query(
    UserCallbackFactory.filter(F.page.in_(TimerButtons.__annotations__)))
async def callback_start_timer(callback: CallbackQuery,
                               callback_data: UserCallbackFactory,
                               state: FSMContext,
                               scheduler: AsyncIOScheduler) -> Union[Message, bool]:
    scheduler_list: list = (await state.get_data()).get("scheduler", [])
    sleep_time: int = getattr(DataTimer, callback_data.page).value
    job = scheduler.add_job(sending_a_timer_callback,
                            trigger="date",
                            run_date=await TimeService.add_time(time=sleep_time),
                            kwargs={"callback": callback, "callback_data": callback_data})
    scheduler_list.append(job)
    await state.update_data(scheduler=scheduler_list)
    return await callback.message.edit_text(
        text=CommandText.setTimer.format(sleepTime=getattr(TimerButtons, callback_data.page).value),
        reply_markup=await Factories.factory_menu(callback_factory=UserCallbackFactory,
                                                  sizes=await KeyboardResize.two_one(
                                                      count_main_buttons=len(StartButtons),
                                                      count_any_buttons=0),
                                                  buttons=StartButtons))
