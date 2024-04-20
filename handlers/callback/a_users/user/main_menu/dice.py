from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.methods import EditMessageText
from aiogram.types import CallbackQuery

from detaTemplates.data_templates import FacetsDice
from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import StartButtons, MainCommands, DiceButtons
from lexicon.ru.text_lexicon import MessageText
from service.scriptsService.dice_service import DiceService

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == StartButtons.dice.name))
async def callback_dice(callback: CallbackQuery, callback_data: UserCallbackFactory) -> None:
    await callback.message.edit_text(text=MessageText.timer,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         sizes=(2, 1),
                                         buttons=DiceButtons,
                                         back_page=callback_data.page,
                                         back=MainCommands.start.name
                                     ))


@router.callback_query(
    UserCallbackFactory.filter(F.page.in_(DiceButtons.__annotations__)))
async def callback_dice_game(callback: CallbackQuery,
                             callback_data: UserCallbackFactory) -> EditMessageText:
    try:
        match callback_data.page:
            case DiceButtons.hexagonal.name | DiceButtons.twenty_sided.name:
                return callback.message.edit_text(
                    text=MessageText.dice.format(
                        number=await DiceService.random_dice(
                            facets=getattr(FacetsDice, callback_data.page).value
                        )
                    ),
                    reply_markup=await Factories.factory_menu(
                        callback_factory=UserCallbackFactory,
                        sizes=(2, 1),
                        buttons=DiceButtons,
                        back_page=callback_data.back_page,
                        back=MainCommands.start.name
                    )
                )
            case DiceButtons.double_hexagonal.name:
                first = await DiceService.random_dice(
                    facets=FacetsDice.double_hexagonal.value
                )

                second = await DiceService.random_dice(
                    facets=FacetsDice.double_hexagonal.value
                )
                return callback.message.edit_text(
                    text=MessageText.dice.format(
                        number=MessageText.double_dice.format(
                            first=first,
                            second=second
                        )
                    ),
                    reply_markup=await Factories.factory_menu(
                        callback_factory=UserCallbackFactory,
                        sizes=(2, 1),
                        buttons=DiceButtons,
                        back_page=callback_data.back_page,
                        back=MainCommands.start.name
                    )
                )
    except TelegramBadRequest:
        await callback.answer()
