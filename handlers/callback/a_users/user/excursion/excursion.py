from aiogram import Router, F
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import ExcursionButtons, MainCommands
from lexicon.ru.text_lexicon import ExcursionText, BackText

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page.in_({ExcursionButtons.wardrobe.name,
                                                              ExcursionButtons.back_wardrobe.name})))
async def callback_wardrobe(callback: CallbackQuery, callback_data: UserCallbackFactory) -> None:
    await callback.message.edit_text(text=getattr(ExcursionText, callback_data.page),
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=(ExcursionButtons.first_hall,),
                                         back=MainCommands.start.name,
                                         sizes=(1, 1)
                                     ))


@router.callback_query(UserCallbackFactory.filter(F.page == ExcursionButtons.first_hall.name))
async def callback_first_hall(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text=ExcursionText.firstHall,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=(ExcursionButtons.second_hall,
                                                  ExcursionButtons.back_wardrobe),
                                         back=MainCommands.start.name,
                                         back_name=BackText.backInStart,
                                         sizes=(1, 1, 1)
                                     ))


@router.callback_query(UserCallbackFactory.filter(F.page == ExcursionButtons.second_hall.name))
async def callback_second_hall(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text=ExcursionText.secondHall,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=(ExcursionButtons.third_hall,
                                                  ExcursionButtons.back_wardrobe),
                                         back=MainCommands.start.name,
                                         back_name=BackText.backInStart,
                                         sizes=(1, 1, 1)
                                     ))


@router.callback_query(UserCallbackFactory.filter(F.page == ExcursionButtons.third_hall.name))
async def callback_third_hall(callback: CallbackQuery) -> None:
    await callback.message.edit_text(text=ExcursionText.thirdHall,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=(ExcursionButtons.back_wardrobe,),
                                         back=MainCommands.start.name,
                                         back_name=BackText.backInStart,
                                         sizes=(1, 1)
                                     ))
