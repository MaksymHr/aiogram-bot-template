import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv


async def main():
    """
    The main variables are defined: config (to load token, admin list, etc), dispatcher and bot.
    Polling starts in this function.

    You can use this function to load all necessary variables or other constructions: middlewares, filters, etc.

    :return:
    """

    # TODO: change logging library to journald

    # Activate logging
    from settings import activate_logging
    await activate_logging()
    logging.info("Bot starting...")

    # loading content from .env file
    load_dotenv()

    # below creating or loading main bot variables
    from settings import BotConfig
    config = BotConfig()

    bot = Bot(token=config.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    # start polling server
    # TODO: create function on_startup to notice admins
    await dp.start_polling(bot)

    logging.info("Bot had been started successfully.")


# Bot start
if __name__ == "__main__":
    asyncio.run(main())
