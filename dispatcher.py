from aiogram import Bot, Dispatcher
import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)
