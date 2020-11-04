import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
POSTGRES_USER = str(os.getenv("POSTGRES_USER"))
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
admins = [
    os.getenv("ADMIN_ID"),
]
URL_APPLES = str(os.getenv("URL_APPLES"))
URL_PEAR = str(os.getenv("URL_PEAR"))
ip = os.getenv("ip")
# db_host = ip  # Если вы запускаете базу не через докер!
PG_HOST = 'database-1.co2ehvjv8n6t.us-east-2.rds.amazonaws.com'
# PG_HOST = "db"  # Если вы запускаете базу через докер и у вас в services стоит название базы db
POSTGRES_URI = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}/{POSTGRES_DB}'
aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}
# webhook settings
WEBHOOK_HOST = f"https://{ip}"
WEBHOOK_PORT = 8443
WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '0.0.0.0'  # or ip
WEBAPP_PORT = os.getenv("WEBAPP_PORT")

WEBHOOK_SSL_CERT = "webhook_cert.pem"
WEBHOOK_SSL_PRIV = "webhook_pkey.pem"

# POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
# POSTGRES_URI = f"postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{db_host}/{DATABASE}"
