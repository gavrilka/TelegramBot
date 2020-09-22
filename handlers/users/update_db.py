from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.markdown import hcode

from loader import dp, db


@dp.message_handler(Command("email"))
async def bot_get_email(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой имейл")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await db.update_user_email(email, message.from_user.id)
    user = await db.select_user(id=message.from_user.id)
    await message.answer("Данные обновлены. Запись в БД: \n" +
                         hcode("id={id}\n"
                               "name={name}\n"
                               "email={email}".format(**user)))
    await state.finish()
