from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:121297.@localhost:5432/fastapi_db"

# Veritabanı bağlantısını oluştur
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency olarak kullanılacak fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
