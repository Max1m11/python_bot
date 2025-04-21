import logging
import asyncio
from os import getenv
from sys import exit
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = getenv("BOT_TOKEN")
if not API_TOKEN:
    exit("Error: no token provided")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_func(message: types.Message):
    await message.answer('Вы ввели команду /start')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
