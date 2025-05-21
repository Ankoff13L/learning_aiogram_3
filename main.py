from aiogram import Bot, Dispatcher
# 13- импортируем Message из модуля aiogram.types
from aiogram.types import Message  
# 10- импортируем модуль asyncio
import asyncio

# 1- создадим переменную token, в которую поместим tokem бота
token = '7966550454:AAErfUdzk2_808sVzNlpD6I3mVrEtSrXOjw'

"""
11- асинхронная функция для обработки нажатия пользователем на кнопку /start
"""
# 12- пуст аргумент message принимает объект Message, а аргумент bot объект Bot
async def get_start(message: Message, bot: Bot):
    # 14- приветсвуем пользователя сообщением. Для этого получаем его чат-id из объекта message 
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}. Рад тебя видеть!')
    await message.answer(f'Привет {message.from_user.first_name}. Рад тебя видеть!') # 15
    await message.reply(f'Привет {message.from_user.first_name}. Рад тебя видеть!') # 16- с помощью метода .reply() мы будем цитировать сообщения пользователя

"""
git
5- вынесем запуск бота в отдельную асинхронную функцию
"""
async def start():
    # 2- создадим объект класса Bot и передадим в него аргументом token от бота
    bot = Bot(token=token)

    # 3- создадим объект класса 
    # 3- Dispather - это объект, который занимается получением update
    dp = Dispatcher()

    # 4- чтобы получить update запустим polling > dp.start_polling()

    # 6- будем запускать polling с ключевым словом await (ждать)> await dp.start_polling()
    # await dp.start_polling()
    # 7- обернём метод вызова await dp.start_polling() в конструкцию > try: ... finally: ... - для гарантированного 
    # закрытия сессии бота после окончания вызова
    try:
        await dp.start_polling()
    finally:
        # 8- в блоке finally будем закрывать сессию бота
        await bot.session.close()

# 9- асинхронно запустим функцию start()
if __name__ == '__main__':
    asyncio.run(start())
    
   