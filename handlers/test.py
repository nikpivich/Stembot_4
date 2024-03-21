'Timur 963427039'
'Alex 845187507'

from aiogram import Router,F
from aiogram.types import Message

router = Router()

@router.message(F.text == 'test')
async def cmd_test(message: Message):
    msg = 'Привет, хозяин'
    if message.from_user.id in (845187507,963427039):
        await message.answer(msg)
    else:
        await message.answer('Ты мусор')