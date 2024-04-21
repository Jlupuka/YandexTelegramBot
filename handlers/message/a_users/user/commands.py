import re
from enum import Enum
from typing import Type

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from factory.factory import UserCallbackFactory
from handlers_scheduler.user.timer import sending_a_timer_message
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import StartButtons, MainCommands, ExcursionButtons
from lexicon.ru.text_lexicon import CommandText, ErrorText, MessageText, ExcursionText, PoemsText
from service.botSerivce.keyboard_resize import KeyboardResize
from service.scriptsService.poems_service import PoemsService
from service.scriptsService.scheduler_service import SchedulerService
from service.scriptsService.time_service import TimeService
from states.states import FSMPoems

router: Router = Router()


@router.message(Command(commands=[MainCommands.start.name]))
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(None)
    await message.answer(text=MessageText.start,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=await KeyboardResize.two_one(
                                 count_main_buttons=len(StartButtons),
                                 count_any_buttons=0),
                             buttons=StartButtons,
                             back_page=MainCommands.start.name
                         ))


@router.message(Command(commands=[MainCommands.time.name]))
async def command_time(message: Message) -> None:
    await message.answer(text=CommandText.nowTime.format(nowTime=await TimeService.now_time()))


@router.message(Command(commands=[MainCommands.date.name]))
async def command_date(message: Message) -> None:
    await message.answer(text=CommandText.nowDate.format(nowDate=await TimeService.now_date()))


@router.message(Command(commands=[MainCommands.set_timer.name]))
async def command_set_timer(message: Message,
                            command: CommandObject,
                            scheduler: AsyncIOScheduler,
                            state: FSMContext
                            ) -> Message:
    if command.args and re.match(r"^-?\d*\.?\d+$", command.args):
        if 0 < (sleep_time := float(command.args)) < 1000:
            scheduler_list: list = (await state.get_data()).get("scheduler", [])
            job = scheduler.add_job(sending_a_timer_message,
                                    trigger="date",
                                    run_date=await TimeService.add_time(time=sleep_time),
                                    kwargs={"message": message, "sleep_time": sleep_time})
            scheduler_list.append(job)
            await state.update_data(scheduler=scheduler_list)
            return await message.answer(text=CommandText.setTimer.format(sleepTime=sleep_time))
        return await message.answer(text=ErrorText.rangeTimer)
    return await message.answer(text=ErrorText.typeTimer)


@router.message(Command(commands=[MainCommands.close.name]))
async def command_close(message: Message, state: FSMContext, scheduler: AsyncIOScheduler) -> Message:
    if user_scheduler := (await state.get_data()).get("scheduler"):
        for job in await SchedulerService.current_data(all_scheduler=scheduler.get_jobs(),
                                                       user_scheduler=user_scheduler):
            job.remove()
        await state.clear()
        return await message.answer(text=CommandText.close,
                                    reply_markup=await Factories.factory_menu(
                                        callback_factory=UserCallbackFactory,
                                        sizes=await KeyboardResize.two_one(
                                            count_main_buttons=len(StartButtons),
                                            count_any_buttons=0),
                                        buttons=StartButtons,
                                    ))
    return await message.answer(text=ErrorText.emptyTimer,
                                reply_markup=await Factories.factory_menu(
                                    callback_factory=UserCallbackFactory,
                                    sizes=await KeyboardResize.two_one(
                                        count_main_buttons=len(StartButtons),
                                        count_any_buttons=0),
                                    buttons=StartButtons,
                                ))


@router.message(Command(commands=[MainCommands.excursion.name]))
async def command_excursion(message: Message) -> None:
    await message.answer(text=ExcursionText.startExcursion,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=(1, 1),
                             buttons=(ExcursionButtons.wardrobe,),
                             back=MainCommands.start.name
                         ))


@router.message(Command(commands=[MainCommands.poems.name]))
async def command_poems(message: Message, state: FSMContext) -> None:
    buttons: Type[Enum] = await PoemsService.authors_for_button()
    await state.update_data(authors={author.name: author.value for author in buttons})
    await message.answer(text=PoemsText.authorMenu,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             buttons=buttons,
                             sizes=await KeyboardResize.two_one(
                                        count_main_buttons=len(buttons),
                                        count_any_buttons=1),
                             back=MainCommands.start.name,
                             back_page=MainCommands.poems.name
                         ))
    await state.set_state(FSMPoems.author)


