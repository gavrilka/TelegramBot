from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit
# Добавляем фильтр IsPrivate
from filters import IsPrivate

@rate_limit(5, 'help')
@dp.message_handler(CommandHelp(), IsPrivate())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/email - Записать email пользователя в базу',
        '/help - Получить справку',
        '/weather - Узнать погоду с помощью сервиса OpenWeatherMap',
        '/fixer - Узнать курс обмена валюты c помощью сервиса fixer.io'
    ]
    await message.answer('\n'.join(text))
