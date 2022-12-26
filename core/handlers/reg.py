from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# списки сотр и руковод
supervisor = []
empolyee = []

async def func_reg(message: Message):
    await message.answer('вы руководитель или сотрудник?', reply_markup=reg_button(1))

# инлайн кнопка
def reg_button(_):
    kb = InlineKeyboardBuilder()
    kb.button(text="руководитель", callback_data="руководитель")
    kb.button(text="сотрудник", callback_data="сотрудник")

    kb.adjust(1)
    return kb.as_markup()

# обработка запроса
async def reg_check(call: CallbackQuery):

    if call.data == "руководитель":
        if call.from_user.username in supervisor:
            await call.answer("вы уже руководитель")
        elif call.from_user.username not in supervisor:
            supervisor.append(call.from_user.username)
            await call.message.edit_text("🎉вы успешно добавлены!")
            await call.message.answer(
                '🤔чтобы посмотреть список сотрудников или руководителей напишите <b>сотрудники</b> или <b>руководители</b>')

    elif call.data == "сотрудник":
        if call.from_user.username in empolyee:
            await call.answer("вы уже сотрудник")
        elif call.from_user.username not in empolyee:
            empolyee.append(call.from_user.username)
            await call.message.edit_text("🎉вы успешно добавлены!")
            await call.message.answer(
                '🤔чтобы посмотреть список сотрудников или руководителей напишите <b>сотрудники</b> или <b>руководители</b>')



# список руководителей
async def func_sup(message: Message):
    sup_sum = len(supervisor)
    if sup_sum == 0:
        await message.answer("на данный момент нет никах руководителей(")
    elif sup_sum != 0:
        for i in range(sup_sum):
            await message.answer(f"@{supervisor[i]}")

# список сотрудников
async def func_empl(message: Message):
    empl_sum = len(empolyee)
    if empl_sum == 0:
        await message.answer("на данный момент нет никах сотрудников(")
    elif empl_sum != 0:
        for i in range(empl_sum):
            await message.answer(f"@{empolyee[i]}")









