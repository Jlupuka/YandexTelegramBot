from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, StartButtons
from lexicon.ru.text_lexicon import MessageText
from service.botSerivce.keyboard_resize import KeyboardResize

router: Router = Router()


@router.message(Command(commands=[MainCommands.stop.name]))
async def stop_servey(message: Message, state: FSMContext) -> None:
    scheduler = (await state.get_data()).get("scheduler")
    await state.clear()
    await message.answer(text=MessageText.stop,
                         reply_markup=await Factories.factory_menu(
                             callback_factory=UserCallbackFactory,
                             sizes=await KeyboardResize.two_one(
                                 count_main_buttons=len(StartButtons),
                                 count_any_buttons=0),
                             buttons=StartButtons,
                             back_page=MainCommands.start.name
                         )
                         )
    if scheduler:
        await state.update_data(scheduler=scheduler)
