from aiogram import Bot, types

async def set_default_commands(bot: Bot):
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Запустить бота"),
            types.BotCommand(command="help", description="Вывести справку"),
            types.BotCommand(command="one", description="Вывести справку"),
            types.BotCommand(command="two", description="Вывести справку"),
        ]
    )