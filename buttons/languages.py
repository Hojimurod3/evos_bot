from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



languages = ReplyKeyboardMarkup([
    [KeyboardButton(text="🇷🇺 rus"),KeyboardButton(text="🇺🇿 O'zbekcha")],
    [KeyboardButton(text="⬅️ Назад")],

],   resize_keyboard=True)