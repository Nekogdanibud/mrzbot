from aiogram import types, F
from ..router import admin_router

@admin_router.message(commands=["admin"])
async def admin_panel(message: types.Message):
    await message.answer("Админ-панель:")

@admin_router.message(F.text == "Статистика")
async def show_stats(message: types.Message):
    await message.answer("Статистика бота...")
