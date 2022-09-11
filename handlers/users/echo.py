from aiogram import filters, types
from dispatcher import dp
from filters import CommandBot

# handle private messages

@dp.message_handler(filters.CommandStart())
async def start(message:types.Message):
    await message.answer("Hello")

# Use specified filter
@dp.message_handler(CommandBot())
async def bot_command(message:types.Message):
    text = message.text.removeprefix("/bot ")
    await message.answer(f"You said: {text}")

@dp.message_handler(filters.Text)
async def echo(message:types.Message):
    await message.answer(message.text)


