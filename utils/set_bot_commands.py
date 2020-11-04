from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("next", "Check whois birthday is next"),
        types.BotCommand("birthday", "add members birthday"),
        types.BotCommand("weather", "Check weather"),
    ])
