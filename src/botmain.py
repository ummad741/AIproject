import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher

# Local files
from bot.handlers import commands
from bot import config

# example

async def main():
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_routers(
        commands.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# projectni strukturasi va run qiladigan functionlari
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")