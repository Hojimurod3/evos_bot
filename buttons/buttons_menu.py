

from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



menu_uz = ReplyKeyboardMarkup([
    [KeyboardButton(text="🏢 О компании"),KeyboardButton(text="📍 Филиалы")],
    [KeyboardButton(text="💼 Вакансии")],
    [KeyboardButton(text="📱 Меню"),KeyboardButton(text="🗣 Новости")],
    [KeyboardButton(text="📞 Контакты/Адрес"),KeyboardButton(text="🇺🇿/🇷🇺 Язык")]
],   resize_keyboard=True)
