from aiogram import executor
from dispatcher import dp
from utils.set_bot_commands import set_default_commands
import filters
import handlers

async def on_startup(dp):
    await set_default_commands(dp)

if __name__ == "__main__":
    print("OK")
    executor.start_polling(dp, on_startup=on_startup)