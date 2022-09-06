from aiogram.dispatcher import filters
from aiogram import types

class CommandBot(filters.BoundFilter):
    async def check(self, message:types.Message) -> bool:
        return message.text.startswith("/bot")