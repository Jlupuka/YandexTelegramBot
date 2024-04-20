from typing import Type, Union

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from factory.factory import UserCallbackFactory
from lexicon.ru.text_lexicon import Default


class Factories:
    @staticmethod
    async def factory_menu(
            callback_factory: Type[UserCallbackFactory],
            sizes: tuple[int, ...],
            buttons=None,
            back: Union[str, bool] = False,
            back_page: Union[str, None] = None,
            back_name: str = Default.backName,
    ) -> InlineKeyboardMarkup:
        if buttons is None:
            buttons = {}
        kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
        kb_builder.row(
            *[
                InlineKeyboardButton(
                    text=data.value,
                    callback_data=callback_factory(
                        page=data.name,
                        back_page=back_page
                    ).pack()
                )
                for data in buttons
            ]
        )
        if back:
            kb_builder.add(
                InlineKeyboardButton(
                    text=back_name,
                    callback_data=callback_factory(
                        page=back, back_page=back_page
                    ).pack(),
                )
            )
        kb_builder.adjust(*sizes)
        return kb_builder.as_markup(resize_keyboard=True)
