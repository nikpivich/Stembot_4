

food_names = ['По-Домашнему', "Барбекю", "Тереяки"]
food_size = ['Маленькая', "Середняя", "Большая"]

from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from keyboards.simple_row import make_row_keyboard
from states import OrderFood


router = Router()

@router.message(StateFilter(None), Command('food'))
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
    await state.update_data(food=message.text)
    await message.answer(
        text = 'Теперь выберите размер порции',
        reply_markup=make_row_keyboard(food_size)
    )
    await state.set_state(OrderFood.food_size)

@router.message(
    OrderFood.food_size,
    F.text.in_(food_size)
)
async def food_size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f'Ваш выбор {message.text} порцию {user_data["food"]}\n'
             f'Возьмите еще десерт: / ',
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()

@router.message(StateFilter(OrderFood.food_name))
async def food_incorrectly(message: Message):
    await message.answer(
        text='У нас нет такой позиции. \n'
             'Выберите из списка ниже:',
        reply_markup=make_row_keyboard(food_names)
    )

@router.message(StateFilter(OrderFood.food_size))
async def food_size_incorrectly(message: Message):
    await message.answer(
        text='У нас нет такого размера порции. \n'
             'Выберите из списка ниже:',
        reply_markup=make_row_keyboard(food_size)
    )































