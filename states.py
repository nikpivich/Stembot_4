from aiogram.fsm.state import StatesGroup, State


class Gen(StatesGroup):
    image_prompt = State()


class OrderFood(StatesGroup):
    food_name = State()
    food_size = State()