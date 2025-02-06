from aiogram import Bot
from aiogram.types import Message


async def start_answer(message: Message):
    await message.answer("Assalomu aleykum, botga xush kelibsiz. Bu bot orqali kanal adminiga savol va takliflaringizni yuborishingiz mumkin.")


async def help_command(message: Message):
    await message.answer("Bu bot yordamida faqat kanal adminiga savol va takliflaringizni yozishingiz mumkin.")


async def send_message(message: Message):
    user_id = message.from_user.id
    text = message.text
    bot = message.bot  # Bot obyektini message ichidan olish

    await bot.send_message(
        1959880466,
        f"Yangi xabar:\n{text}\n\nFoydalanuvchi ID: {user_id}\nUsername: @{message.from_user.username}"
    )

    await message.answer("Xabaringiz adminga yuborildi. Admin javob yozishini kuting!")


ADMIN_ID = 1959880466  # O'zingizning Telegram ID raqamingizni shu yerga yozing


async def reply_to_user(message: Message):
    bot = message.bot  # Bot obyektini olish

    # Admin tekshiruvi
    if message.from_user.id != ADMIN_ID:
        await message.answer("Siz admin emassiz! Ushbu komandadan foydalana olmaysiz.")
        return

    command_parts = message.text.split(maxsplit=2)

    if len(command_parts) < 3:
        await message.answer("Xatolik! Format: /reply <user_id> <xabar>")
        return

    user_id = command_parts[1]
    reply_text = command_parts[2]

    try:
        user_id = int(user_id)
        await bot.send_message(user_id, f"Admin javobi: {reply_text}")
        await message.answer("Xabar foydalanuvchiga yuborildi ✅")
    except ValueError:
        await message.answer("Xatolik! User ID noto‘g‘ri.")
