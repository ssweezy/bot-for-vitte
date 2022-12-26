from aiogram.types import Message
import json

# команда /start
async def func_start(message: Message):
    await message.answer("добро пожаловать в нашу компанию! помощь - /help")

# команда /help
async def func_help(message: Message):
    await message.reply('●/reg - зарегистрироваться\n🕵🏼по всем вопросам обращайтесь к @boombaxbaby')

# эхо
async def func_eho(message: Message):
    await message.answer(message.text)

