from aiogram import Router, F
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()

@router.message(Command("ban"), F.reply_to_message)
async def cmd_ban(message: Message, admins: set[int]):
    if message.from_user.id not in admins:
        await message.answer(
            "У вас недостаточно прав для совершения этого действия"
        )
    else:
        await message.chat.ban(
            user_id=message.reply_to_message.from_user.id
        )
        await message.answer("Нарушитель заблокирован")