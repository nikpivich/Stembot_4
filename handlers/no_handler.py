from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def no_handler(messege: Message):
    await messege.answer('Я не знаю как ответить на это сообщение')