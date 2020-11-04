from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit
from filters import IsPrivate

@rate_limit(limit=10)
@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    username = message.from_user.username
    language_code = message.from_user.language_code
    await commands.add_user(id=message.from_user.id,
                            name=name, username=username,language_code=language_code)

    count = await commands.count_users()
    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Твой язык по умолчанию: {language_code}',
                f'Твой юзернейм: {username}',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользователей',
            ]))
