from aiogram.fsm.state import StatesGroup, State


class BookEssaySt(StatesGroup):
    date = State()
    time = State()
    proof = State()
    confirm = State()


class ParticipateInAnEventSt(StatesGroup):
    proof = State()
    confirm = State()


class FillingDataSt(StatesGroup):
    name = State()
    age = State()
    phone = State()