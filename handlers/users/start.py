import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        await db.add_user(id=message.from_user.id,
                          name=name)
    except asyncpg.exceptions.UniqueViolationError:
        pass
    count = await db.count_users()
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользователей',
            ]))
