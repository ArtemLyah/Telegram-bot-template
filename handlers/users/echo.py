from aiogram import filters, types
from dispatcher import dp
from filters import CommandBot
from databases import User

# handle private messages

@dp.message_handler(filters.CommandStart())
async def start(message:types.Message):
    await message.answer("Hello")

# Use specified filter
@dp.message_handler(CommandBot())
async def bot_command(message:types.Message, user:User):
    text = message.text.removeprefix("/bot ")
    await message.answer(
        f"You said: {text}\n"
        f"Your name is {user.name}\n"
        f"Your age is {user.age}"
    )

@dp.message_handler(filters.Text)
async def echo(message:types.Message):
    await message.answer(message.text)


