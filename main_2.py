from aiogram import Bot, Dispatcher
from aiogram.types import Message  
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


"""
11- асинхронная функция для обработки нажатия пользователем на кнопку /start
"""
async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}. Рад тебя видеть!')
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть!') 
    await message.reply(f'Привет {message.from_user.first_name}. Рад тебя видеть!') 
    

"""
ассинхронная функция для запуска бота
"""
async def start():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
    