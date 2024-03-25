from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from keyboards import for_base


router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f"Приветствую тебя {message.from_user.username}, {message.from_user.id} \n"
                         f"Я бот с множнством функций. Вот некоторые",
                         reply_markup=for_base.menu)


@router.message(Command('menu'))
@router.callback_query(F.data('menu'))
@router.message(F.text.lower() == 'меню')
@router.message(F.text.lower() == 'выйти в меню')
async def cmd_menu(message: Message):
    await message.answer('Меню', reply_markup=for_base.menu)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Нет помощи')