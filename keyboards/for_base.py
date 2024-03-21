from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text= 'Генерация текста', callback_data='generate_text'),
     InlineKeyboardButton(text='Генерация изображения', callback_data='generate_image')],
    [InlineKeyboardButton(text='Помощь', callback_data='help')]
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выйти в меню')]], resize_keyboard=True)
iexit_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Выйти в меню', callback_data='menu')]])