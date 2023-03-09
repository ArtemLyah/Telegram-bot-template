from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def build_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.add(KeyboardButton("1"))
    builder.add(KeyboardButton("2"))
    builder.add(KeyboardButton("3"))

    return builder.as_markup(resize_keyboard=True)