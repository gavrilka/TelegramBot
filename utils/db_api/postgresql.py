import asyncio

import asyncpg
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self, pool):
        self.pool: Pool = pool

    @classmethod
    async def create(cls):
        pool = await asyncpg.create_pool(
            user=config.PGUSER,
            password=config.PGPASSWORD,
            host=config.ip,
        )
        return cls(pool)

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id INT NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            PRIMARY KEY (id)
            );
"""
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num + 1}" for num, item in enumerate(parameters)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, id: int, name: str, email: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, Name, email) VALUES($1, $2, $3)
        """
        await self.pool.execute(sql, id, name, email)

    async def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = f"""
        SELECT * FROM Users WHERE 
        """
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval("SELECT COUNT(*) FROM Users")

    async def update_user_email(self, email, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Users SET email=$1 WHERE id=$2
        """
        return await self.pool.execute(sql, email, id)

    async def delete_users(self):
        await self.pool.execute("DELETE FROM Users WHERE TRUE")