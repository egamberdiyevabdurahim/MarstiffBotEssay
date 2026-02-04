from aiogram.fsm.state import StatesGroup, State


class CreateEventSt(StatesGroup):
    name = State()
    cost = State()
    date = State()
    hour = State()
    video = State()
