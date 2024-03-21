from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    image_prompt = State()