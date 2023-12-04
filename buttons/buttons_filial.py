from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


filial = ReplyKeyboardMarkup([
    [KeyboardButton(text="☕️ Показать ближайший филиал")],
    [KeyboardButton(text="🏢 Головной офис")],
    [KeyboardButton(text="г. Ташкент")],
    [KeyboardButton(text="back")]
],   resize_keyboard=True)


Tashkent = ReplyKeyboardMarkup([
    [KeyboardButton(text="📍 Samarqand Darvoza"),KeyboardButton(text="📍 Алайский базар")],
    [KeyboardButton(text="📍 Малика"),KeyboardButton(text="📍 Яхъё Гулямова, 94")],
    [KeyboardButton(text="Back")]
   ],   resize_keyboard=True)


location = ReplyKeyboardMarkup([
    [KeyboardButton(text="отправить локацию",request_location=True)],[KeyboardButton(text="Back")]
],   resize_keyboard=True)