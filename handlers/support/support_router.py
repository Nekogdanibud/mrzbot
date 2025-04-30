from aiogram import Router, types, F
from aiogram.filters import Command
from core.filters import IsSupport

support_router = Router(name="support_router")

# Фильтры можно комбинировать через запятую (логическое И)
@support_router.message(Command("support"), IsSupport)
async def admin_panel(message: types.Message):
    await message.answer("👑 Админ-панель")

@support_router.message(F.text == "Статистика", IsSupport)
async def show_stats(message: types.Message):
    await message.answer("📊 Статистика бота...")

