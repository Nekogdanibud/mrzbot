from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from typing import Any, Dict, Union
from typing import Union, List, Set

class RoleFilter(BaseFilter):
    def __init__(self, required_role: str):
        self.required_role = required_role

    async def __call__(self, event: Union[Message, CallbackQuery], **kwargs) -> bool:
        # Извлекаем role напрямую из kwargs
        role = kwargs.get('role')
        if role is None:
            return False  # Возвращаем False, если role отсутствует
        
        # Проверяем соответствие роли
        return role == self.required_role

class HasAnyRole(BaseFilter):
    def __init__(self, roles: Union[List[str], Set[str], str]):
        if isinstance(roles, str):
            roles = {roles}
        self.allowed_roles = set(roles)

    async def __call__(self, message: Message, role: str, **kwargs) -> bool:
        return role in self.allowed_roles


# Экземпляры фильтров для разных ролей
IsAdmin = RoleFilter('admin')
IsSupport = RoleFilter('support')
IsUser = RoleFilter('user')
IsBanned = RoleFilter('banned')
IsStaff = HasAnyRole({"admin", "support"}) 
IsNotBanned = HasAnyRole({"user", "admin", "support"})
