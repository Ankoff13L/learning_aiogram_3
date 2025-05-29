# https://aiogram.dev/
# пример бота с главной страницы
# импорт модулей для получения Токена из файла .env
from dotenv import load_dotenv, find_dotenv
from os import getenv

# импорт модулей для построения бота
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message


load_dotenv(find_dotenv())
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет! Я бот, созданный с помощью aiogram.")

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main()) 