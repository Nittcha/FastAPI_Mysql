from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal

# ฟังก์ชันสำหรับรับ dependency injection ของ DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# สร้าง dependency สำหรับ FastAPI route ให้ใช้งาน DB session
db_dependency = Annotated[Session, Depends(get_db)]