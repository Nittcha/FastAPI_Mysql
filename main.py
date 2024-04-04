from fastapi import FastAPI, HTTPException, status
from .dependencies import db_dependency
from pydantic import BaseModel
from database import engine
import models

app = FastAPI()
# สร้างตารางในฐานข้อมูลโดยอ้างอิงจากโมเดลที่นิยามใน SQLAlchemy
models.Base.metadata.create_all(bind=engine)

# นิยาม Pydantic model สำหรับการตรวจสอบข้อมูลของ Post ก่อนที่จะบันทึกลงในฐานข้อมูล
class PostBase(BaseModel):
    title: str
    content: str
    user_id: int

# นิยาม Pydantic model สำหรับการตรวจสอบข้อมูลของ User ก่อนที่จะบันทึกลงในฐานข้อมูล
class UserBase(BaseModel):
    username: str  # สมมติว่าคอลัมน์ในฐานข้อมูลชื่อ 'username'


# สร้าง endpoint สำหรับการสร้างโพสต์ใหม่
@app.post("/posts/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_posts(post: PostBase, db: db_dependency):
    db_post = models.Post(**post.dict())  # สร้างอินสแตนซ์ของโมเดล Post
    db.add(db_post)  # เพิ่มโพสต์ใหม่ลงใน DB session
    db.commit()  # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล

# สร้าง endpoint สำหรับการอ่านโพสต์ตาม ID
@app.get("/posts/{posts_id}", status_code=status.HTTP_200_OK, response_model=None)
async def read_post(post_id: int, db: db_dependency):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()  # ค้นหาโพสต์ในฐานข้อมูล
    if post is None:  # ถ้าไม่พบโพสต์
        raise HTTPException(status_code=404, detail='Post was not found')  # โยนข้อผิดพลาด HTTP 404
    return post  # ถ้าพบโพสต์ ส่งกลับโพสต์นั้น

# สร้าง endpoint สำหรับการลบโพสต์ตาม ID
@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=None)
async def delete_post(post_id: int, db: db_dependency):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()  # ค้นหาโพสต์ในฐานข้อมูล
    if db_post is None:  # ถ้าไม่พบโพสต์
        raise HTTPException(status_code=404, detail="Post not found")  # โยนข้อผิดพลาด HTTP 404
    db.delete(db_post)  # ลบโพสต์จาก DB session
    db.commit()  # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล

# สร้าง endpoint สำหรับการสร้างผู้ใช้ใหม่
@app.post("/users/", status_code=status.HTTP_201_CREATED, response_model=None)
async def create_user(user: UserBase, db: db_dependency):
     db_user = models.User(**user.dict())  # สร้างอินสแตนซ์ของโมเดล User
     db.add(db_user)  # เพิ่มผู้ใช้ใหม่ลงใน DB session
     db.commit()  # ยืนยันการเปลี่ยนแปลงในฐานข้อมูล

# สร้าง endpoint สำหรับการอ่านข้อมูลผู้ใช้ตาม ID
@app.get("/users/{user_id}", status_code=status.HTTP_200_OK, response_model=None)
async def read_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()  # ค้นหาผู้ใช้ในฐานข้อมูล
    if user is None:  # ถ้าไม่พบผู้ใช้
        raise HTTPException(status_code=404, detail='User not found')  # โยนข้อผิดพลาด HTTP 404
    return user  # ถ้าพบผู้ใช้ ส่งกลับข้อมูลผู้ใช้นั้น

