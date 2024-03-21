from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from keyboards import for_questions


router = Router()


@router.message(Command('qwe'))
async def cmd_question(message: Message):
    await message.answer(
        'Вы в ресурсе?',
        reply_markup=for_questions.get_yes_no()
    )

@router.message(F.text.lower() == 'да')
async def answer_yes(message: Message):
    await message.answer(
        'Отлично, поработаем',
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower() == 'нет')
async def answer_no(message: Message):
    await message.answer(
        'Плохо, отдыхаем',
        reply_markup=ReplyKeyboardRemove()
    )
