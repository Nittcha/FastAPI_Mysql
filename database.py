from sqlalchemy import create_engine # สร้างตัวเชื่อมต่อ (engine) กับฐานข้อมูล
from sqlalchemy.orm import sessionmaker # session ที่จะใช้เพื่อจัดการ transactions กับฐานข้อมูล
from sqlalchemy.ext.declarative import declarative_base # base class สำหรับโมเดลของคุณ ซึ่งทุกโมเดลจะสืบทอดจาก base class นี้

# นี่คือ URL สำหรับเชื่อมต่อกับฐานข้อมูล MySQL
# มันประกอบด้วย username, password, host, port และ database name
URL_DATABASE = "mysql+pymysql://root:@localhost:3306/admin_test"

# สร้าง engine ที่ใช้ในการเชื่อมต่อและการทำงานกับฐานข้อมูล
engine = create_engine(URL_DATABASE)

# สร้าง factory function สำหรับ session ที่กำหนดค่าให้ไม่ auto commit และไม่ auto flush
# และผูกมันกับ engine ที่เราสร้างไว้เพื่อใช้ในการเชื่อมต่อกับฐานข้อมูล
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# สร้าง base class สำหรับ declarative ใน SQLAlchemy
# โมเดลทั้งหมดที่เราจะสร้างจะต้องสืบทอดจาก class นี้
Base = declarative_base()
