# worker_settings.py
import asyncio
from arq import Worker

# ฟังก์ชันที่จะรับข้อมูล (Job data) มาแสดงผล
async def simple_work(ctx, job_data):
    print(f"📦 [Job ID: {ctx['job_id']}] กำลังประมวลผลข้อมูล: {job_data}")
    # จำลองการใช้เวลาทำงาน 2 วินาที
    await asyncio.sleep(2) 
    print(f"✅ งานเสร็จสมบูรณ์!")
    return f"Success: {job_data}"

# การตั้งค่าสำหรับ ARQ Worker
class WorkerSettings:
    # ระบุฟังก์ชันที่ Worker สามารถทำงานได้
    functions = [simple_work]
    
    # (Optional) หาก Redis ของคุณมีรหัสผ่าน หรืออยู่คนละพอร์ต สามารถตั้งค่า redis_settings ได้ที่นี่
    # จากค่าเริ่มต้น มันจะเชื่อมต่อไปที่ localhost:6379