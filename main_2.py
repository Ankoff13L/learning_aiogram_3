from aiogram import Bot, Dispatcher
from aiogram.types import Message  
import asyncio

token = '7966550454:AAErfUdzk2_80fjhkkjdhkdfjhfkjhjkh'

"""
11- асинхронная функция для обработки нажатия пользователем на кнопку /start
"""
async def get_start(message: Message, bot: Bot):

    

"""
ассинхронная функция для запуска бота
"""
async def start():
    bot = Bot(token=token)
    dp = Dispatcher()
    
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
    