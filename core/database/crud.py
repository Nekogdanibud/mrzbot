from .models import Session, User
from datetime import datetime

# Добавление нового пользователя
def create_user(telegram_id: int):
    session = Session()
    user = User(telegram_id=telegram_id, registration_date=datetime.now())
    session.add(user)
    session.commit()
    session.close()

# Получение пользователя по telegram_id
def get_user(telegram_id: int) -> User:
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    session.close()
    return user

# Обновление роли пользователя
def update_user_role(telegram_id: int, role: str):
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if user:
        user.role = role
        session.commit()
    session.close()

# Удаление пользователя
def delete_user(telegram_id: int):
    session = Session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
