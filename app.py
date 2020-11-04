from aiogram.utils.executor import start_webhook

from data.config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, admins
from loader import SSL_CERTIFICATE, ssl_context, bot, db
from utils.set_bot_commands import set_default_commands
from utils.db_api import db_gino


async def on_startup(dp):

    # Check webhook
    webhook = await bot.get_webhook_info()

    # If URL is bad
    if webhook.url != WEBHOOK_URL:
        # If URL doesnt match current - remove webhook
        if not webhook.url:
            await bot.delete_webhook()

    await bot.set_webhook(
        url=WEBHOOK_URL,
        certificate=SSL_CERTIFICATE
    )
    import filters
    import middlewares
    filters.setup(dp)
    middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify
    # await db.create_table_users()
    print("Подключаем БД")
    await db_gino.on_startup(dp)
    print("Готово")

    # print("Чистим базу")
    # await db.gino.drop_all()
    #
    # print("Готово")

    print("Создаем таблицы")
    await db.gino.create_all()

    print("Готово")
    await on_startup_notify(dp)
    await set_default_commands(dp)


# async def on_shutdown(dp):
    # insert code here to run it before shutdown

    # Send message to admin
    # await bot.send_message(admins[0], "Я выключен!")

    # Close bot
    # await bot.close()

    # Close DB connection (if used)
    # await dp.storage.close()
    # await dp.storage.wait_closed()


if __name__ == '__main__':
    from handlers import dp
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=ssl_context
    )