import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен бота из переменных окружения
API_TOKEN = os.getenv('API_TOKEN')

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Обработчик для команды /start
@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [
        types.KeyboardButton(text="Кнопка 1"),
        types.KeyboardButton(text="Кнопка 2"),
        types.KeyboardButton(text="Кнопка 3")
    ]
    keyboard.add(*buttons)
    await message.answer("Привет! Пожалуйста, выберите одну из кнопок ниже:", reply_markup=keyboard)

# Обработчик для нажатия кнопок (ReplyKeyboard)
@dp.message()
async def handle_reply_buttons(message: types.Message):
    if message.text == "Кнопка 1":
        await message.answer("Вы нажали Кнопку 1")
    elif message.text == "Кнопка 2":
        await message.answer("Вы нажали Кнопку 2")
    elif message.text == "Кнопка 3":
        await message.answer("Вы нажали Кнопку 3")
    else:
        await message.answer("Извините, я не понимаю эту команду.")
# Основной асинхронный цикл для запуска бота
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")
    except Exception as e:
        logging.error(f"Ошибка при запуске бота: {e}")