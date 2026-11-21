import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

# загружаем переменные из .env
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

# настраиваем подключение
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


# табличка (описание)
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    role = Column(String(50), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)


# Проверяем логин пароль
def get_user(username, password):
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(username=username, password=password).first()
        return user
    finally:
        session.close()