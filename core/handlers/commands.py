from aiogram.types import BotCommandScopeDefault, BotCommand
from aiogram import Bot

async def func_commands(bot: Bot):
    commands = [
        BotCommand(
            command="start",
            description="начало"
        ),
        BotCommand(
            command="help",
            description="помощь"
        ),
        BotCommand(
            command="reg",
            description="регистрация"
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
