from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from .callback_datas import SendExtraData

kb = [
    [InlineKeyboardButton(text="Write to bot", switch_inline_query_current_chat="hello")],
    [InlineKeyboardButton(text="Send data", callback_data="text")],
    [InlineKeyboardButton(text="Send extra data", callback_data=SendExtraData(message="hello", type_="qwe").pack())],
]

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=kb)