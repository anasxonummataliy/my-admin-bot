from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.filters import Command
from asyncio import run
import function

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(1959880466, "Bot started✅")

async def shutdown_answer(bot : Bot):
    await bot.send_message(1959880466, "Bot stopped⛔️")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(function.start_answer, Command("start"))
    dp.message.register(function.help_command, Command("help"))
    dp.message.register(function.reply_to_user, Command("reply"))
    dp.message.register(function.send_message)




    dp.shutdown.register(shutdown_answer)
    bot = Bot("7924738206:AAFTXfyjZsY_pB_0gg-VGM9Vez3sZsvbBfA")
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Botni qayta ishga tushurish."),
            BotCommand(command="/help", description="Yordam"),
        ]
    )
    await dp.start_polling(bot, polling_timeout=1)

run(start())
