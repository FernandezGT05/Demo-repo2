from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine=create_engine("sqlite:///database.db")
SessionLocal=sessionmaker(autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
