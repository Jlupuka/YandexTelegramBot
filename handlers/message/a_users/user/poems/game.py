from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from factory.factory import UserCallbackFactory
from keyboard.factory.keboard import Factories
from lexicon.ru.buttons_lexicon import MainCommands, PoemsButtons
from lexicon.ru.text_lexicon import PoemsText, BackText, ErrorText
from states.states import FSMPoems

router: Router = Router()


@router.message(StateFilter(FSMPoems.play))
async def play_poem_handler(message: Message, state: FSMContext) -> Message:
    state_data = (await state.get_data())
    poem = state_data["userPoem"]
    user_index = state_data["userIndex"]
    if message.text == poem[user_index]:
        if user_index >= len(poem) - 2:
            return await message.answer(text=PoemsText.endGame.format(
                poemText="\n".join(poem)
            ),
                reply_markup=await Factories.factory_menu(
                    callback_factory=UserCallbackFactory,
                    sizes=(1,),
                    back_name=BackText.backInStart,
                    back=MainCommands.start.name
                ))
        user_index += 2
        await state.update_data(userIndex=user_index)
        return await message.answer(text=PoemsText.nextGame.format(
            poemText="\n".join(poem[:user_index])
        ),
            reply_markup=await Factories.factory_menu(
                callback_factory=UserCallbackFactory,
                sizes=(1,),
                back_name=BackText.backInStart,
                back=MainCommands.start.name
            ))
    return await message.answer(text=ErrorText.poemText,
                                reply_markup=await Factories.factory_menu(
                                    callback_factory=UserCallbackFactory,
                                    buttons=(PoemsButtons.hint,),
                                    sizes=(1, 1),
                                    back_name=BackText.backInStart,
                                    back=MainCommands.start.name
                                )
                                )
