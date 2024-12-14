from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import asyncio

# Токен бота
API_TOKEN = "7635257187:AAFix2SsQXIMJbOhM9ek52SE1Y4wq_za_n0"

# Ініціалізація бота та диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Створення інлайн-клавіатури
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Дуже Важлива інформація", url="https://t.me/c/2282611931/1")],
        [InlineKeyboardButton(text="Питання", url="https://t.me/c/2282611931/5")]
    ]
)

# Обробник команди /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Оберіть тематичний чат \n❗Для початку вам порібно перейти за посиланням https://t.me/+2RtgBcKiaadhZjE6 та стати учасником чату", reply_markup=inline_keyboard)

# Основна функція для запуску бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
