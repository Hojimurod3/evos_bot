from aiogram import Bot,Dispatcher, executor, types

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove


vakansiya = ReplyKeyboardMarkup([
    [KeyboardButton(text="Ташкент"),KeyboardButton(text="Андижан")],
    [KeyboardButton(text="Коканд"),KeyboardButton(text="Наманган")],
    [KeyboardButton(text="Ташкентская область"),KeyboardButton(text="Самарканд")],
    [KeyboardButton(text="Фергана"),KeyboardButton(text="Хорезмская область")],
    [KeyboardButton(text="Навои")],
    [KeyboardButton(text="back ↩️")]



   ], resize_keyboard=True
)
work = ReplyKeyboardMarkup([
    [KeyboardButton(text="Универсальный сотрудник"),KeyboardButton(text="Оператор Call центра")],
    [KeyboardButton(text="Повар")],
    [KeyboardButton(text="↩️ Back")]

    ], resize_keyboard=True
)
worker = ReplyKeyboardMarkup([
    [KeyboardButton(text="nomer qoldirish",request_contact=True)],
    [KeyboardButton(text="Back ↩️")]
    ], resize_keyboard=True
)
