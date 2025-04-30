from aiogram import Router, types
from aiogram.filters import Command
from core.filters import IsUser

user_router = Router(name="user_router")

@user_router.message(Command("start"), IsUser)
async def start_handler(message: types.Message):
    await message.answer("Вы обычный пользователь!")

@user_router.message(Command("debug"))
async def debug_handler(message: types.Message, role: str):
    await message.answer(f"Ваша роль: {role}\nID: {message.from_user.id}")
