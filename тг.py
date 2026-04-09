import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Вместо 'ВАШ_ТОКЕН' нужно вставить ключ, который даст BotFather
TOKEN = '8748398370:AAHR2dtjak-fmzvvdr3nz2t7CeHzZvs19o4'

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я бот, написанный на Python. Отправь мне что-нибудь!")

# Эхо-режим: бот повторяет ваше сообщение
@dp.message()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")