from aiogram import types
from loader import dp
from filters import IsGroup
from aiogram.dispatcher.filters import Command
from utils.db_api import quick_commands as commands
from asyncpg import UniqueViolationError
import datetime


@dp.message_handler(Command("birthday", prefixes="!/"),
                    regexp=r"^[!/]birthday ([a-zA-Z0-9_]+)? (\d\d)?-?(\d\d)-?(\d\d\d\d)?")
async def birthday(message: types.Message):
    data = message.text.split(" ")
    governor = data[1]
    birthdate = data[2]
    b = birthdate.split('-')
    day = int(b[0])
    month = int(b[1])
    year = int(b[2])
    d = datetime.date(year, month, day)
    text_added = f'Governors *{governor}* birthday *{d.strftime("%d %B %Y")}* is added to database'
    text_updated = f'Governors *{governor}* birthday *{d.strftime("%d %B %Y")}* is updated'
    try:
        await commands.add_birthday(governor=governor, date=d)
        await message.answer(text_added, parse_mode='Markdown')
    except UniqueViolationError:
        await message.answer(text_updated, parse_mode='Markdown')
        await commands.update_birthday(governor=governor, date=d)
    except Exception as e:
        await message.answer('I am sorry, *' + message.from_user.first_name + '*,incorrect input',
                             parse_mode='Markdown')
        print(e)

@dp.message_handler(Command("next", prefixes="!/"))
async def birthday(message: types.Message):
    if message.text == '/next' or message.text == '!next':
        name = await commands.next_birthday()
        await message.answer(f'Next birthday is *{name.governor}* {name.date.strftime("%d %B")} ',
                             parse_mode='Markdown')
    else:
        await message.answer('Incorrect input',
                             parse_mode='Markdown')


@dp.message_handler(Command("next3", prefixes="!/"))
async def birthday(message: types.Message):
    if message.text == '/next3' or message.text == '!next3':
        name = await commands.next3_birthday()
        print(name)
        await message.answer(f'Next 3 birthday are \n'
                             f'*{name[0][0]}* - {name[0][1].strftime("%d %B")}\n'
                             f'*{name[1][0]}* - {name[1][1].strftime("%d %B")}\n'
                             f'*{name[2][0]}* - {name[2][1].strftime("%d %B")}\n',
                             parse_mode='Markdown')
    else:
        await message.answer('Incorrect input',
                             parse_mode='Markdown')