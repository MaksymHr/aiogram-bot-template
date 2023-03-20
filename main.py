import asyncio

from aiogram import Bot, Dispatcher


async def main():
    """
    The main variables are defined: config (to load token, admin list, etc), dispatcher and bot.
    Polling starts in this function.

    You can use this function to load all necessary variables or other constructions: middlewares, filters, etc.

    :return:
    """

    # TODO: integrate logging

    bot = Bot(token="12345:qwerty")
    dp = Dispatcher()

    # start polling server
    # TODO: create function on_startup to notice admins
    await dp.start_polling(bot)


# Bot start
if __name__ == "__main__":
    asyncio.run(main())
