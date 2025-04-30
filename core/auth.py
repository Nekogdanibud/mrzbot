from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.database.models import User, get_session

async def get_user(telegram_id: int) -> User | None:
    async with get_session()() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalar_one_or_none()

async def get_user_role(telegram_id: int) -> str | None:
    user = await get_user(telegram_id)
    return user.role if user else None

async def create_user(telegram_id: int, role: str = 'user') -> User:
    async with get_session()() as session:
        user = User(telegram_id=telegram_id, role=role)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
