import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5718017404:AAGRgucvqZRDP7ozkvtp4s3PNrhoGL-IFnU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
    await message.reply('Starting all processes...')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
    await message.reply('Looking for information about myself through whole net...')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)