import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.utils.executor import start_polling

# Tokenni xavfsizlik uchun server muhitidan (Environment Variable) olamiz
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrug'i kelganda ishlaydigan qism
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Men serverda bepul ishlayotgan sinov botiman. Istalgan matnni yozing, men uni qaytaraman!")

# Oddiy xabarlarni aks-sado (echo) qilib qaytarish
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())