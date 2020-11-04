from typing import List

from aiogram import Dispatcher
from gino import Gino
import sqlalchemy as sa
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, DateTime, sql, TIMESTAMP, Boolean, JSON)
from aiogram import types, Bot

from data import config

db = Gino()


# Пример из https://github.com/aiogram/bot/blob/master/app/models/db.py

# # Новый код user
# class User(db.Model):
#     __tablename__ = 'users'
#
#     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
#     user_id = Column(BigInteger)
#     language = Column(String(2))
#     full_name = Column(String(100))
#     username = Column(String(50))
#     # referral = Column(Integer)
#     query: sql.Select
#
#     def __repr__(self):
#         return "<User(id='{}', fullname='{}', username='{}')>".format(
#             self.id, self.full_name, self.username)

# class DBCommands:
#
#     async def get_user(self, user_id):
#         user = await User.query.where(User.user_id == user_id).gino.first()
#         return user
#
#     async def add_new_user(self, referral=None):
#         user = types.User.get_current()
#         old_user = await self.get_user(user.id)
#         if old_user:
#             return old_user
#         new_user = User()
#         new_user.user_id = user.id
#         new_user.username = user.username
#         new_user.full_name = user.full_name
#
#         if referral:
#             new_user.referral = int(referral)
#         await new_user.create()
#         return new_user
#
#     async def set_language(self, language):
#         user_id = types.User.get_current().id
#         user = await self.get_user(user_id)
#         await user.update(language=language).apply()
#
#     async def count_users(self) -> int:
#         total = await db.func.count(User.id).gino.scalar()
#         return total
#
#     async def check_referrals(self):
#         bot = Bot.get_current()
#         user_id = types.User.get_current().id
#
#         user = await User.query.where(User.user_id == user_id).gino.first()
#         referrals = await User.query.where(User.referral == user.id).gino.all()
#
#         return ", ".join([
#             f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
#             for num, referral in enumerate(referrals)
#         ])

    # async def show_items(self):
    #     items = await Item.query.gino.all()
    #
    #     return items

class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=db.func.now(),
                        onupdate=db.func.now(),
                        server_default=db.func.now())


async def on_startup(dispatcher: Dispatcher):
    print("Установка связи с PostgreSQL")
    await db.set_bind(config.POSTGRES_URI)