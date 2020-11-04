from sqlalchemy import Integer, Column, BigInteger, String, sql, DateTime, Sequence

from utils.db_api.db_gino import TimedBaseModel

#Класс таблицы user
class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    language_code = Column(String(2))
    username = Column(String(50))
    referral = Column(BigInteger)

    query: sql.Select

#Класс таблицы birthday
class Birthday(TimedBaseModel):
    __tablename__ = 'birthdays'
    governor = Column(String(100), primary_key=True)
    date = Column(DateTime())
    query: sql.Select
