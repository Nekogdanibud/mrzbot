from aiogram import Router, types, F
from aiogram.filters import Command
from core.filters import IsAdmin

admin_router = Router(name="admin_router")

# Фильтры можно комбинировать через запятую (логическое И)
@admin_router.message(Command("admin"), IsAdmin)
async def admin_panel(message: types.Message):
    await message.answer("👑 Админ-панель")

@admin_router.message(F.text == "Статистика", IsAdmin)
async def show_stats(message: types.Message):
    await message.answer("📊 Статистика бота...")

@admin_router.message(Command("myrole"))
async def show_role(message: types.Message, role: str):
    await message.answer(f"Ваша роль: {role}")
