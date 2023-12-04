from aiogram import Bot,Dispatcher, executor, types
from buttons.buttons_menu import menu_uz
from buttons.buttons_vakansy import vakansiya,work,worker
from buttons.buttons_filial import filial,Tashkent,location
from aiogram.types import InputFile
from buttons.languages import languages

API_TOKEN='6460684839:AAHps-3sFzzDuDdb4SPiLfdvAjvri83zS7M'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def start_evos_bot(message: types.Message):
    await message.answer(text=message.text, reply_markup=menu_uz)

@dp.message_handler(text='📍 Филиалы')
async def filiall(message: types.Message):
    # photo_url = 'blob:https://web.telegram.org/b07eeedf-a06b-4a8c-be51-aa507709602e'

    # await bot.send_photo(message.chat.id, photo=photo_url, caption='EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто 49 торговых точек и современное многопрофильное производство.Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!')
    await message.answer(text=message.text, reply_markup=filial)

@dp.message_handler(text='г. Ташкент')
async def city(message: types.Message):
    await message.answer(text=message.text, reply_markup=Tashkent)

@dp.message_handler(text='☕️ Показать ближайший филиал')
async def filials(message: types.Message):
    await message.answer(text=message.text, reply_markup=location)

@dp.message_handler(text='🏢 Головной офис')
async def main_office(message: types.Message):
    await message.answer(text="Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.\nОриентир: MAKRO THE TOWER")
    latitude = 41.317381
    longitude = 69.253106
    await message.answer_location(latitude=latitude, longitude=longitude)





@dp.message_handler(text='🏢 О компании')
async def information(message: types.Message):
    photo_path = 'photo/img.png'

    await bot.send_photo(message.chat.id, photo=InputFile(photo_path), caption="""'Информация о компании:Сеть ресторанов быстрого обслуживания EVOS® не стоит \nна месте, а постоянно растет и развивается вместе с вами \nи для вас! Мы расширяем свою географию и открываем \nновые филиалы практически каждый месяц. \nСейчас в нашей сети насчитывается более 50 филиалов по \nвсему Узбекистану. Поэтому мы всегда в поиске \nдинамичных и активных людей, которые хотят стать \nчастью нашей команды и готовы строить свою карьеру в \nEVOS®. \nEVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и \nперспективы карьерного роста. \nНачни свою карьеру в EVOS® уже сейчас!""")




@dp.message_handler(text='💼 Вакансии')
async def vacansy(message: types.Message):
    await message.answer(text="Vakansiya taqdim etildi:", reply_markup=vakansiya)






@dp.message_handler(text='📱 Меню')
async def menu(message: types.Message):
    photo_path = 'photo/img_2.png'
    link_url = 'https://evos.uz/'
    link_url_2 = 'https://www.instagram.com/evosuzbekistan/'
    link_url_3 = 'https://t.me/evosdeliverybot'
    link_url_4 = 'https://www.facebook.com/evosuzbekistan/'


    message_text = f"[Перейти на сайт Evos]({link_url}).\n[instagram]({link_url_2})|[Telegram]({link_url_3})|[Facebook]({link_url_4})"
    await bot.send_photo(message.chat.id, photo=InputFile(photo_path))
    await bot.send_message(message.chat.id, text=message_text, parse_mode=types.ParseMode.MARKDOWN)




@dp.message_handler(text='🗣 Новости')
async def news(message: types.Message):
      await message.answer(text="Kompaniya yangiliklari\nAksiya\nYangi filiallar\nYangi tortlar va hk.")

@dp.message_handler(text='📞 Контакты/Адрес')
async def phone_adress(message: types.Message):
      photo_path = 'photo/img_1.png'

      await bot.send_photo(message.chat.id, photo=InputFile(photo_path),caption="📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.\n📌Ориентир: MAKRO THE TOWER\n\n📲 Контакты: +998 71 203 12 12")
      await message.answer(text="📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.\n📌Ориентир: MAKRO THE TOWER\n\n📲 Контакты: +998 71 203 12 12")
      latitude = 41.317381
      longitude = 69.253106
      await message.answer_location(latitude=latitude, longitude=longitude)




@dp.message_handler(text='Ташкент')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Андижан')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Коканд')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Наманган')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Ташкентская область')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Самарканд')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Фергана')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Хорезмская область')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Навои')
async def city(message: types.Message):
    await message.answer(text="ishlarni korib chiqsangiz", reply_markup=work)

@dp.message_handler(text='Универсальный сотрудник')
async def city(message: types.Message):
    await message.answer(text="contact ningizni qoldiring va tez orada aloqaga chiqamiza:", reply_markup=worker)

@dp.message_handler(text='Оператор Call центра')
async def city(message: types.Message):
    await message.answer(text="contact ningizni qoldiring va tez orada aloqaga chiqamiza:", reply_markup=worker)

@dp.message_handler(text='Повар')
async def city(message: types.Message):
    await message.answer(text="contact ningizni qoldiring va tez orada aloqaga chiqamiza:", reply_markup=worker)

@dp.message_handler(text='Back ↩️')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=work)

@dp.message_handler(text='back ↩️')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=menu_uz)

@dp.message_handler(text='↩️ Back')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=vakansiya)

@dp.message_handler(text='↩️ Back')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=vakansiya)

@dp.message_handler(text='Back')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=filial)

@dp.message_handler(text='back')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=menu_uz)

@dp.message_handler(text='🇺🇿/🇷🇺 Язык')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=languages)

@dp.message_handler(text='⬅️ Назад')
async def orqaga(message: types.Message):
    await message.answer(text="Siz orqaga qayttiz", reply_markup=menu_uz)

@dp.message_handler(text='📍 Samarqand Darvoza')
async def filial_adress(message: types.Message):
      photo_path = 'photo/img_3.png'

      await bot.send_photo(message.chat.id, photo=InputFile(photo_path),caption="""Филиал  "Самарканд дарвоза"\n\nАдрес: ул. Коратош, 5А""")
      latitude = 41.316427
      longitude = 69.230965
      await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(text='📍 Алайский базар')
async def filial_adress(message: types.Message):
      photo_path = 'photo/img_4.png'

      await bot.send_photo(message.chat.id, photo=InputFile(photo_path),caption="""Филиал: Алайский базар\n\nАдрес: просп. Амира Темура, 42\n\nКонтакты: +998 71 203 12 12""")
      latitude = 41.319999
      longitude = 69.282571
      await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(text='📍 Малика')
async def filial_adress(message: types.Message):
      photo_path = 'photo/img_5.png'

      await bot.send_photo(message.chat.id, photo=InputFile(photo_path),caption="""Филиал: Малика\n\nАдрес: ул. Богиравон, 29\n\nКонтакты: +998 71 203 12 12""")
      latitude = 41.342806
      longitude = 69.264684
      await message.answer_location(latitude=latitude, longitude=longitude)

@dp.message_handler(text='📍 Яхъё Гулямова, 94')
async def filial_adress(message: types.Message):
      photo_path = 'photo/img_6.png'

      await bot.send_photo(message.chat.id, photo=InputFile(photo_path),caption="""Филиал: улица Яхъё Гулямова, 94\n\nАдрес: улица Яхъё Гулямова, 94\n\nКонтакты: +998 71 203 12 12""")
      latitude = 41.304757
      longitude = 69.284565
      await message.answer_location(latitude=latitude, longitude=longitude)


if __name__ == '__main__':
    print("bot ishga tushdi")
    executor.start_polling(dp, skip_updates=False)