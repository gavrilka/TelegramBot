import ssl

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_gino import db
from data import config
from data.config import WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# db = dp.loop.run_until_complete(Database.create())
__all__ = ["bot", "storage", "dp", "db"]
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
SSL_CERTIFICATE = open(WEBHOOK_SSL_CERT, "rb").read()
ssl_context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)