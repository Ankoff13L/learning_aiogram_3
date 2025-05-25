# """
# В этом примере функция my_corutine приостанвливает своё выполнение на 3 секунды, 
# позваляя в это время выполняться другим задачам, если бы они были.
# """

# import asyncio
    
# async def my_coroutine():       # объявляем асинхронную функцию my_coroutine()   
#     print('Начало корутины')    # 4_печать: Начало корутины
#     await asyncio. sleep(3)     # 5_корутина приостанавливается, управление возвращается в событийный 
#                                 # цикл (Event Loop), т.к. других задач нет, цикл "засыпает" на  3 сек.
#     print('Корутина завершена') # через 3 сек. цикл (Event Loop) возобноляет выполнение my_coroutine()
#                                 # 6_идёт печать: Корутина завершена

# async def main():           # объявляем асинхронную функцию main(), которая запускает await my_coroutine()
#     await my_coroutine()    # 3_выпоняется await my_coroutine(), управление передаётся в my_coroutine()

# asyncio.run(main())         # 1_ asyncio.run() создаёт новый событийный цикл (Event Loop) 
#                             # 2_ и запускается корутина main()
# """
# Завершение работы. 
# - my_coroutine() завершается, управление возвращается в main()
# - main() завершается, событийный цикл закрывается
# """


# import asyncio

# async def task_1():
#     print("Task_1: Start")
#     await asyncio.sleep(2)
#     print("Task_1: Start")


# async def task_2():
#     print("Task_2: Start")
#     await asyncio.sleep(1)
#     print("Task_2: Start")


# async def main():
#     await asyncio.gather(task_1(), task_2())

# asyncio.run(main())






import asyncio

async def my_task():
    print("Мои задачи")

async def main():
    await my_task()

asyncio.run(main())

