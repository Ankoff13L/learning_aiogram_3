#################################################################################################
# # библиотеки для токена
# from dotenv import load_dotenv, find_dotenv
# from os import getenv
# # библиотеки для aiogram
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command
# from aiogram import F
# # форматирование текста
# from aiogram.enums import ParseMode

# # Добавляем значение токена в проект
# load_dotenv(find_dotenv())
# TOKEN = getenv("BOT_TOKEN")

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token=TOKEN)
# # Диспетчер
# dp = Dispatcher()

# # Хэндлер на команду /start
# @dp.message(F.text, Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Привет *Босс*\!", parse_mode=ParseMode.MARKDOWN_V2)

# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())

#################################################################################################
# Пример форматирования вводимого текса с помощью aiogram.utils.formating

# from dotenv import load_dotenv, find_dotenv
# from os import getenv

# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import Command

# from aiogram.utils.formatting import Bold, as_list, as_marked_section, as_key_value, HashTag

# load_dotenv(find_dotenv())
# TOKEN = getenv("BOT_TOKEN")

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)
# # Объект бота
# bot = Bot(token=TOKEN)
# # Диспетчер
# dp = Dispatcher()

# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     # Формируем сложное сообщение с разметкой
#     content = as_list(
#         as_marked_section(
#             Bold("Успешно:"),
#             "Тест 1",
#             "Тест 3",
#             "Тест 4",
#             marker="✅ ",
#         ),
#         as_marked_section(
#             Bold("Ошибка:"),
#             "Тест 2",
#             marker="❌ ",
#         ),
#         as_marked_section(
#             Bold("Итого:"),
#             as_key_value("  Всего", 4),
#             as_key_value("  Успешно", 3),
#             as_key_value("  Ошибка", 1),
#             marker=" ",
#         ),
#         HashTag("#test"),
#         sep="\n\n",
#     )
#     # Отправляем сообщение с форматированием
#     await message.answer(**content.as_kwargs())

# if __name__ == "__main__":
#       asyncio.run(dp.start_polling(bot))

#################################################################################################
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

##################################################################################################
# # Cинтаксис обработчика команды `/start` диспетчером:
# # библиотеки для токена
# from dotenv import load_dotenv, find_dotenv
# from os import getenv
# # библиотеки для aiogram
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.filters.command import CommandStart

# # Добавляем значение токена в проект
# load_dotenv(find_dotenv())
# TOKEN = getenv("BOT_TOKEN")

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TOKEN) # Создаём объект бот
# dp = Dispatcher() # Создаём диспетчер	 

# # Обработчик команды /start
# @dp.message(CommandStart())  # Ловим сообщения ТОЛЬКО с командой /start
# async def cmd_start(message: types.Message):
#     await message.answer("Привет! 👋 Я твой новый бот. Рад знакомству!")
    
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main()) # Запускаем асинхронную функцию main()


# # ##################################################################################################
# # Cинтаксис обработчика команды `/help` с роутером:
# # библиотеки для токена
# from dotenv import load_dotenv, find_dotenv
# from os import getenv
# # библиотеки для aiogram
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher, types, Router
# from aiogram.filters.command import Command

# # Добавляем значение токена в проект
# load_dotenv(find_dotenv())
# TOKEN = getenv("BOT_TOKEN")

# # Включаем логирование, чтобы не пропустить важные сообщения
# logging.basicConfig(level=logging.INFO)

# bot = Bot(token=TOKEN) # Создаём объект бот
# dp = Dispatcher() # Создаём диспетчер	 

# router = Router()  # Создаем роутер
# dp.include_router(router) # Подключаем наш роутер с командами к диспетчеру

# # Обработчик команды /help
# @router.message(Command("help"))  # Ловим сообщения ТОЛЬКО с командой /help
# async def cmd_help(message: types.Message):
#     help_text = "Вот что я умею:\n"
#     help_text += "/start - Начать работу с ботом\n"
#     help_text += "/help - Получить справку\n"
#     help_text += "/menu - Показать меню действий"
#     await message.answer(help_text)
    
# # Запуск процесса поллинга новых апдейтов
# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main()) # Запускаем асинхронную функцию main()

#################################################################################################
# Пример с одним роутером и тремя обработчиками
# библиотеки для токена
from dotenv import load_dotenv, find_dotenv
from os import getenv
# библиотеки для aiogram
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters.command import Command,CommandStart

# Добавляем значение токена в проект
load_dotenv(find_dotenv())
TOKEN = getenv("BOT_TOKEN")

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN) # Создаём объект бот
dp = Dispatcher() # Создаём диспетчер	 

commands_router = Router()  # Создаем роутер
dp.include_router(commands_router) # Подключаем наш роутер с командами к диспетчеру

# Обработчик команды /start
@commands_router.message(CommandStart())  # Ловим сообщения ТОЛЬКО с командой /start
async def cmd_start(message: types.Message):
    await message.answer("Привет! 👋 Я твой новый бот. Рад знакомству!")


# Обработчик команды /help
@commands_router.message(Command("help"))  # Ловим сообщения ТОЛЬКО с командой /help
async def cmd_help(message: types.Message):
    help_text = "Вот что я умею:\n"
    help_text += "/start - Начать работу с ботом\n"
    help_text += "/help - Получить справку\n"
    help_text += "/menu - Показать меню действий"
    await message.answer(help_text)

# Обработчик команды /menu
@commands_router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await message.answer("Главное меню:")
    
# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) # Запускаем асинхронную функцию main()

#################################################################################################