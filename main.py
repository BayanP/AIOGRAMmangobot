import random
from os import system
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
from aiogram import Bot # Связь с телеграмм ботом
from aiogram.types import * # Все типы данных aiogram
from aiogram.utils import executor # Для того чтобы наш бот не засыпал
from aiogram.dispatcher import Dispatcher # Наблюдение за чатом

# Created module - Созданный модуль
from core.text import *
from core.config import *
from core.keyboard import *
from core.database import *
from core.utils import get_address

system("clear")
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: Message):
    image = open(random.choice(IMAGE), "rb")
    await message.reply_photo(photo=image, caption=START_CAPTION)
    await message.answer(text=START_CAPTION2, reply_markup=start_markup)
    if CheckRegister(message.from_user.id) is None:
        await message.answer(text=START_CAPTION3)
    else:
        await message.answer(text=START_CAPTION4, reply_markup=auth_menu_markup)


@dp.message_handler(content_types=ContentTypes.CONTACT)
async def get_contact(message: Message):
    user_id = message.contact.user_id
    username = message.chat.username
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    phone = message.contact.phone_number
    RegistrationUserPG(user_id, username, first_name, last_name, phone)
    await message.reply(text=START_CAPTION4, reply_markup=auth_menu_markup)

@dp.message_handler(content_types=ContentTypes.TEXT)
async def message_user(message: Message):
    if CheckRegister(message.from_user.id) is not None:
        if message.text.lower() == "места":
            await message.delete()
            places_markup.inline_keyboard = []
            num = 0
            for loc in get_location():
                num += 1
                places_markup.add(
                    InlineKeyboardButton(text=loc[0], callback_data=f"mesta_{num}")
                )
            places_markup.add(
                InlineKeyboardButton(text="Поиск ...", switch_inline_query_current_chat=""),
            )
            await message.answer(text="Вот 5 мест для вас, для обновление мест нажмите Места еще раз", reply_markup=places_markup)
    else:
        await message.reply(text=START_CAPTION3, reply_markup=start_markup)


@dp.callback_query_handler(text_contains="mesta_")
async def data_location(call: CallbackQuery):
    if call.data and call.data.startswith("mesta_"):
        code = call.data[-1:]
    if code.isdigit():
        code = int(code)
    
    if code == 1:
        for i in call.message.reply_markup.inline_keyboard:
            if i[0]['callback_data'] == call.data:
                try:
                    result = get_name_location(i[0]["text"])
                    text = f"Название: {result[2]}\nКатигория: {result[1]}\nАдрес: {result[3]}\nПодробнее: <a href='{result[4]}'>Нажмите тут</a>"
                   
                    await call.message.edit_text(text, reply_markup=places_markup)
                except:
                    continue
    if code == 2:
        for i in call.message.reply_markup.inline_keyboard:
            if i[0]['callback_data'] == call.data:
                try:
                    result = get_name_location(i[0]["text"])
                    text = f"Название: {result[2]}\nКатигория: {result[1]}\nАдрес: {result[3]}\nПодробнее: <a href='{result[4]}'>Нажмите тут</a>"
                   
                    await call.message.edit_text(text, reply_markup=places_markup)
                except:
                    continue
    if code == 3:
        for i in call.message.reply_markup.inline_keyboard:
            if i[0]['callback_data'] == call.data:
                try:
                    result = get_name_location(i[0]["text"])
                    text = f"Название: {result[2]}\nКатигория: {result[1]}\nАдрес: {result[3]}\nПодробнее: <a href='{result[4]}'>Нажмите тут</a>"
                   
                    await call.message.edit_text(text, reply_markup=places_markup)
                except:
                    continue
    if code == 4:
        for i in call.message.reply_markup.inline_keyboard:
            if i[0]['callback_data'] == call.data:
                try:
                    result = get_name_location(i[0]["text"])
                    text = f"Название: {result[2]}\nКатигория: {result[1]}\nАдрес: {result[3]}\nПодробнее: <a href='{result[4]}'>Нажмите тут</a>"
                   
                    await call.message.edit_text(text, reply_markup=places_markup)
                except:
                    continue
    if code == 5:
        for i in call.message.reply_markup.inline_keyboard:
            if i[0]['callback_data'] == call.data:
                try:
                    result = get_name_location(i[0]["text"])
                    text = f"Название: {result[2]}\nКатигория: {result[1]}\nАдрес: {result[3]}\nПодробнее: <a href='{result[4]}'>Нажмите тут</a>"
                   
                    await call.message.edit_text(text, reply_markup=places_markup)
                except:
                    continue

if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        pass


















    