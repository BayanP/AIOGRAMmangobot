import random
from datetime import datetime
from os import system

# Download libraries
from aiogram import Bot      # Связь с телеграм ботом
from aiogram.types import *  # Все типы данных aiogram
from aiogram.utils import executor          # Для того чтобы наш бот не засыпал
from aiogram.dispatcher import Dispatcher   # Наблюдение за чатом 

from core.config import *
from core.keyboard import *
from core.text import *
from core.database import *
from core.utils import get_adress

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
        await message.answer(text=START_CAPTION4, reply_markup=auth_markup)

@dp.message_handler(content_types=ContentTypes.CONTACT)
async def get_contact(message: Message):
    user_id = message.contact.user_id
    username = message.chat.username
    first_name = message.contact.first_name
    last_name = message.contact.last_name
    phone = message.contact.phone_number
    RegistrationUserPG(user_id, username, first_name, last_name, phone)
    await message.reply(text=START_CAPTION4)

if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        pass