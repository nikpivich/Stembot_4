from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeF


router = Router()
router.message.filter(ChatTypeF(chat_type=['group', 'supergroup']))

@router.message(
    ChatTypeF(chat_type=['group', 'supergroup']),
    Command('dice')
)
async def cmd_dice(message:Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)


@router.message(
    ChatTypeF(chat_type=['group', 'supergroup']),
    Command('dice1')
)
async def cmd_dice1(message:Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)


@router.message(
    ChatTypeF(chat_type=['group', 'supergroup']),
    Command('dice2')
)
async def cmd_dice2(message:Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)


@router.message(
    ChatTypeF(chat_type=['group', 'supergroup']),
    Command('dice3')
)
async def cmd_dice3(message:Message):
    await message.answer_dice(emoji=DiceEmoji.DART)