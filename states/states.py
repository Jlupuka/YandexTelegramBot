from aiogram.fsm.state import StatesGroup, State


class FSMServey(StatesGroup):
    get_city = State()
    get_weather = State()


class FSMPoems(StatesGroup):
    author = State()
    poem = State()
    play = State()