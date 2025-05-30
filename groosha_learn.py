# библиотеки для токена
from dotenv import load_dotenv, find_dotenv
from os import getenv
# библиотеки для aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Добавляем значение токена в проект
load_dotenv(find_dotenv())
TOKEN = getenv("BOT_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет Босс!")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())





# # Пример обработчика с навешеным декоратором  
# # Хэндлер на команду /test1 
# @dp.message(Command("test1"))
# async def cmd_test1(message: types.Message):
#     await message.reply("Test 1")


# # Пример обработчика с вызовом метода регистрации у диспетчера
# # Хэндлер на команду /test2
# async def cmd_test2(message: types.Message):
#     await message.reply("Test 2")

# # Где-то в другом месте, например, в функции main():
# dp.message.register(cmd_test2, Command("test2"))


# if __name__ == "__main__":
#     asyncio.run(main())
