

food_names = ['По-Домашнему', "Барбекю", "Тереяки"]
food_size = ['Маленькая', "Середняя", "Большая"]

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from keyboards.simple_row import make_row_keyboard
from states import OrderFood
router = Router()

@router.message(Command('food'))
async def cmd_food(message:Message, state: FSMContext):
    await message.answer(
        text='Какую шаурму хотите?:',
        reply_markup=make_row_keyboard(food_names)
    )
    await state.set_state(OrderFood.food_name)


@router.message(
    OrderFood.food_name,
    F.text.in_(food_names)
)
async def food_item(message: Message, state : FSMContext):
    await state.update_data(food=message.text.lower())
    await message.answer(
        text = 'Теперь выберите размер порции',
        reply_markup=make_row_keyboard(food_size)
    )
    await state.set_state(OrderFood.food_size)