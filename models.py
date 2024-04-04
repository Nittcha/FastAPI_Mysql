from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# นิยามคลาส User ซึ่งสืบทอดจาก Base class
class User(Base):
    # กำหนดชื่อตารางในฐานข้อมูลเป็น 'users'
    __tablename__ = 'users'

    # นิยามคอลัมน์ 'id' เป็น primary key และเปิดใช้งาน indexing สำหรับคอลัมน์นี้
    id = Column(Integer, primary_key=True, index=True)
    # นิยามคอลัมน์ 'username' ซึ่งเป็น string ความยาว 50 และต้องเป็นค่าที่ไม่ซ้ำในตาราง
    username = Column(String(50), unique=True)

# นิยามคลาส Post ซึ่งสืบทอดจาก Base class
class Post(Base):
    # กำหนดชื่อตารางในฐานข้อมูลเป็น 'posts'
    __tablename__ = 'posts'

    # นิยามคอลัมน์ 'id' เป็น primary key และเปิดใช้งาน indexing สำหรับคอลัมน์นี้
    id = Column(Integer, primary_key=True, index=True)
    # นิยามคอลัมน์ 'title' เป็น string ความยาว 50
    title = Column(String(50))
    # นิยามคอลัมน์ 'content' เป็น string ความยาว 100
    content = Column(String(100))
    # นิยามคอลัมน์ 'user_id' เพื่อเชื่อมต่อกับตาราง 'users'
    user_id = Column(Integer)
