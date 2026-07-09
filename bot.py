import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiohttp import web

# Tokeningizni yozing
TOKEN = "8492276550:AAGeVqXV0cKw_DmxS64inSTU5ilUEt-LPL0"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start buyrog'i
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}! Men Glitch-da bepul va 24/7 ishlayotgan botman!")

@dp.message()
async def echo_message(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Glitch uxlab qolmasligi uchun kichik Web-Sahifa ochamiz
async def handle(request):
    return web.Response(text="Bot ishlamoqda...")

async def main():
    # Web serverni ishga tushirish (Glitch uchun)
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 3000)
    asyncio.create_task(site.start())
    
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
