import asyncio
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

# Асинхронный движок SQLite
DATABASE_URL = "sqlite+aiosqlite:///core/database/database.db"
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    marzban_username = Column(String(50), nullable=True)
    role = Column(String(20), default='user', nullable=False)
    registration_date = Column(TIMESTAMP, server_default=func.now())

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

def get_session():
    return sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

# Автоматическое создание таблиц при первом импорте
asyncio.get_event_loop().run_until_complete(create_tables())
