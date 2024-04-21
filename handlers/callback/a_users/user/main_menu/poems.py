from enum import Enum
from typing import Type

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, PoemsButtons
from lexicon.ru.text_lexicon import PoemsText, BackText
from service.botSerivce.keyboard_resize import KeyboardResize
from service.scriptsService.poems_service import PoemsService
from states.states import FSMPoems

router: Router = Router()


@router.callback_query(UserCallbackFactory.filter(F.page == MainCommands.poems.name))
async def callback_poems(callback: CallbackQuery, state: FSMContext) -> None:
    buttons: Type[Enum] = await PoemsService.authors_for_button()
    await state.update_data(authors={author.name: author.value for author in buttons})
    await callback.message.edit_text(text=PoemsText.authorMenu,
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


@router.callback_query(UserCallbackFactory.filter(F.page.regexp(r"^author_(\d+)$")),
                       StateFilter(FSMPoems.author, FSMPoems.poem))
async def callback_user_author(callback: CallbackQuery,
                               callback_data: UserCallbackFactory,
                               state: FSMContext
                               ) -> None:
    author = (await state.get_data())["authors"][callback_data.page]
    buttons = await PoemsService.poems_for_button(author=author)
    await callback.message.edit_text(text=PoemsText.poemMenu,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=buttons,
                                         sizes=await KeyboardResize.two_one(
                                             count_main_buttons=len(buttons),
                                             count_any_buttons=1),
                                         back=MainCommands.poems.name,
                                         back_page=callback_data.page
                                     ))
    await state.update_data(userAuthor=author, poems={poem.name: poem.value for poem in buttons})
    await state.set_state(FSMPoems.poem)


@router.callback_query(UserCallbackFactory.filter(F.page.regexp(r"^poem_(\d+)$")),
                       StateFilter(FSMPoems.author, FSMPoems.poem))
async def callback_user_poem(callback: CallbackQuery,
                             callback_data: UserCallbackFactory,
                             state: FSMContext
                             ) -> None:
    state_data = await state.get_data()
    poem = state_data["poems"][callback_data.page]
    author = state_data["userAuthor"]
    text_poem = await PoemsService.poem(author=author, poem_name=poem)
    await callback.message.edit_text(text=PoemsText.offerPlay,
                                     reply_markup=await Factories.factory_menu(
                                         callback_factory=UserCallbackFactory,
                                         buttons=(PoemsButtons.play,),
                                         sizes=(1, 1),
                                         back=MainCommands.poems.name
                                     ))
    await state.update_data(userPoem=text_poem.split('\n'))
    await state.set_state(FSMPoems.play)


@router.callback_query(UserCallbackFactory.filter(F.page == PoemsButtons.play.name), StateFilter(FSMPoems.play))
async def callback_start_game(callback: CallbackQuery, state: FSMContext) -> None:
    poem = (await state.get_data())["userPoem"]
    index = 0
    await callback.message.edit_text(text=PoemsText.startGame.format(
        poemText=poem[index]
    ),
        reply_markup=await Factories.factory_menu(
            callback_factory=UserCallbackFactory,
            sizes=(1,),
            back=MainCommands.start.name,
            back_name=BackText.backInStart
        ))
    await state.update_data(userIndex=index + 1)


@router.callback_query(UserCallbackFactory.filter(F.page == PoemsButtons.hint.name), StateFilter(FSMPoems.play))
async def callback_hint(callback: CallbackQuery, state: FSMContext) -> None:
    state_data = (await state.get_data())
    poem = state_data["userPoem"]
    user_index = state_data["userIndex"]
    await callback.message.edit_text(text=PoemsText.hintText.format(
        poemText=poem[user_index]
    ),
        reply_markup=await Factories.factory_menu(
            callback_factory=UserCallbackFactory,
            sizes=(1,),
            back=MainCommands.start.name,
            back_name=BackText.backInStart
        ))
