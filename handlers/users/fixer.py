from loader import dp
import aiohttp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message
from aiogram import types
from aiogram.types.message import ContentTypes
from datetime import datetime
from datetime import time
from datetime import date


async def get_money(currency):
    async with aiohttp.ClientSession() as session:
        api_key = 'a558518dc5bb3e2828fceaa9e264a8c0'
        async with session.get('http://data.fixer.io/api/latest?access_key=' + api_key) as resp:
            response = await resp.json()
            price = float('{:.2f}'.format(response['rates'][currency]))
            # date = response['datetime']

            timestamp = response['timestamp']
            time = datetime.fromtimestamp(timestamp)
            text = f'💰 *1 EUR = {price} {currency}* \n' \
                   f'🕜 {time}\n' \
                   f'📈 from Fixer.io'
            return text

@dp.message_handler(Command("fixer"))
async def money(message: Message):
    if message.text == '/fixer':
        await message.answer(f'Dear *{message.from_user.first_name}*! choose currency, for example /fixer RUB', parse_mode='Markdown')
    else:
        try:
            text = message.text
            texts = text.split(' ')
            currency = str.upper(texts[1])
            await message.answer(await get_money(currency), parse_mode='Markdown')
        except Exception:
            await message.answer(f'Bro *{message.from_user.first_name}*, there is no such pairs, please try again!', parse_mode='Markdown')

