import asyncio

from utils.db_api.postgresql import Database


async def test():
    print("Создаем таблицу Пользователей...")
    await db.create_table_users()
    print("Готово")

    print("Добавляем пользователей")

    await db.add_user(1, "One", "email")
    await db.add_user(2, "Vasya", "vv@gmail.com")
    await db.add_user(3, "1", "1")
    await db.add_user(4, "1", "1")
    await db.add_user(5, "John", "john@mail.com")
    print("Готово")

    users = await db.select_all_users()
    print(f"Получил всех пользователей: {users}")

    user = await db.select_user(Name="John", id=5)
    print(f"Получил пользователя: {user}")


loop = asyncio.get_event_loop()
db = loop.run_until_complete(Database.create())
loop.run_until_complete(test())