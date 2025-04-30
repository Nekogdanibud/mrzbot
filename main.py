import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from core.middleware import AuthMiddleware
from core.database.models import get_session
from handlers import user_router, admin_router, support_router

# Загрузка переменных окружения
from dotenv import load_dotenv
load_dotenv()

async def main():
    # Инициализация бота
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher(storage=MemoryStorage())

    # Подключение middleware
    dp.update.middleware(AuthMiddleware())

    # Регистрация роутеров
    dp.include_router(user_router)
    dp.include_router(support_router)
    dp.include_router(admin_router)

    # Запуск бота
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
