from aiogram.dispatcher.filters.state import State, StatesGroup


class States(StatesGroup):
    MenuState = State()
    RegisterState = State()
    WritingResultState = State()


States = States()
