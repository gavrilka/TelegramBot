from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


# Кастомный фильтр на Приватный чат с ботом
class IsPrivate(BoundFilter):

    # Функция check используется каждый раз когда приходит апдейт, и диспатчер проходит по всем хендлерам и фильтрам,
    # используемых в них
    # Этот фильтр мы будем использовать только для message_handler, и типа Message, поэтому тайпхинт такой
    async def check(self, message: types.Message):
        # Возвращаем результат сравнения типа чата из пришедего сообщения и типа чата "ПРИВАТНЫЙ"
        return message.chat.type == types.ChatType.PRIVATE