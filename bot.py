from utils.set_bot_commands import set_default_commands
from loader import dispatcher, bot
from handlers import users_router, group_router, error_router
from middlewares import LoggingMessageMiddleware, LoggingCallbackMiddleware, LoggingInlineMiddleware
from utils.logs import logger
import asyncio

async def on_startup():
    await set_default_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True) # skip updates
    print("OK")

async def main():
    dispatcher.include_router(users_router)
    dispatcher.include_router(group_router)
    dispatcher.include_router(error_router)

    dispatcher.message.outer_middleware(LoggingMessageMiddleware())
    dispatcher.callback_query.outer_middleware(LoggingCallbackMiddleware())
    dispatcher.inline_query.outer_middleware(LoggingInlineMiddleware())

    logger.debug("Start DiaRatingBot")

    await on_startup()
    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())