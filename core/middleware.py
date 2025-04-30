from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update
from typing import Any, Dict, Callable, Awaitable
from core.auth import get_user_role, create_user

class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        # Получаем реальное событие (Message или CallbackQuery)
        real_event = event.event if hasattr(event, 'event') else event
        
        # Извлекаем user_id в зависимости от типа события
        user_id = None
        if isinstance(real_event, Message):
            user_id = real_event.from_user.id
        elif isinstance(real_event, CallbackQuery):
            user_id = real_event.from_user.id
        
        # Если не удалось получить user_id, пропускаем обработку
        if not user_id:
            return await handler(event, data)
        
        # Получаем или создаем пользователя
        role = await get_user_role(user_id)
        if role is None:
            user = await create_user(user_id)
            role = user.role
        
        # Добавляем роль в data
        data['role'] = role
        
        return await handler(event, data)
