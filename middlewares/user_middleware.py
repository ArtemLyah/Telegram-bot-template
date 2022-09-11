from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from databases import User

class GetDBUserMiddleware(BaseMiddleware):
    # name function on_process_ -> use needed handler (message_handler, callback_query_handler, ...)
    async def on_process_message(self, message:types.Message, data:dict):
        data["user"] = User(name=message.from_user.full_name, age=18)
    async def on_process_callback_query(self, query:types.CallbackQuery, data:dict):
        pass