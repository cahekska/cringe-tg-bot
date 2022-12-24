from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

BTN_RR = InlineKeyboardButton('Не рикролл', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
BTN_HELP = InlineKeyboardButton('Что я умею', callback_data='help')


HELP = InlineKeyboardMarkup().add(BTN_RR)
START = InlineKeyboardMarkup().add(BTN_HELP)
