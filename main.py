from bot_token import token
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from core.handlers.functions import func_start, func_eho, func_help
from core.handlers.reg import func_reg, reg_check, func_empl, func_sup
from core.handlers.commands import func_commands
import asyncio
import logging


TOKEN = token
dp = Dispatcher()


async def on_startup(bot: Bot):
    await func_commands(bot)
    print("Bot started")
async def on_shutdown(bot: Bot):
    print("bot stopped")

# регистрация хендлеров
async def start():
    bot = (Bot(token=TOKEN, parse_mode="HTML"))
    logging.basicConfig(level=logging.INFO)

    # на старте и стопе
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    # остальные хендлеры
    dp.message.register(func_start, Command(commands="start"))
    dp.message.register(func_help, Command(commands="help"))
    dp.message.register(func_reg, Command(commands="reg"))
    dp.callback_query.register(reg_check, F.data.in_(["руководитель","сотрудник"]))
    dp.message.register(func_empl, F.text == "сотрудники")
    dp.message.register(func_sup, F.text == "руководители")

    dp.message.register(func_eho)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())



