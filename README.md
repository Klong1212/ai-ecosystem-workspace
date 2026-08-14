# AI Ecosystem Workspace

โปรเจกต์ AI Ecosystem เป็นระบบที่มีสถาปัตยกรรมแบบ Feature-Based Architecture สำหรับจัดการและให้บริการทางด้าน AI อย่างครบวงจรตั้งแต่การเตรียมข้อมูล, การ Label, การฝึกโมเดล ไปจนถึงการเสิร์ฟโมเดล

## Overview
โปรเจกต์นี้ประกอบไปด้วยระบบ Backend ที่พัฒนาด้วย **FastAPI** และโครงสร้างพื้นฐานที่สนับสนุนการทำงานต่างๆ ดังนี้:
- **PostgreSQL** — ฐานข้อมูลหลัก (Port 5432)
- **Redis** — ระบบ Cache และคิวงาน (Port 6379)
- **MinIO** — ระบบ Object Storage สำหรับจัดเก็บไฟล์ (Ports 9000/9001)
- **Label Studio** — แพลตฟอร์มสำหรับ Data Labeling (Port 8080)
- **ARQ** — Background Job Worker ควบคุมด้วย Redis

## Architecture Diagram
โครงสร้างการทำงานของระบบ:
`End user -> React -> FastAPI -> Redis -> Job Worker <-> Model <-> Trainer Worker`
- **FastAPI -> PostgreSQL**: สำหรับบันทึกข้อมูลหลัก
- **Label Studio -> PostgreSQL**: สำหรับจัดการข้อมูลการ Label
- ฐานข้อมูลจะถูกใช้ร่วมกันระหว่าง Worker และ Trainer (อ้างอิงจาก `diagrams/overview.png`)

## Tech Stack
| เทคโนโลยี | หน้าที่ |
| --- | --- |
| **FastAPI** | Web Framework สำหรับสร้าง API |
| **PostgreSQL** | Relational Database |
| **Redis** | In-memory Data Structure Store (Cache / Queue) |
| **MinIO** | S3 Compatible Object Storage |
| **Label Studio** | Data Annotation Tool |
| **ARQ** | Async Job Queues in Python |
| **uv** | Python Package Manager |
| **Docker Compose** | จัดการ Container สำหรับ Infrastructure |

## โครงสร้างโปรเจกต์ (Directory Structure)
```
.
├── backend/            # โค้ด FastAPI Backend
│   ├── app/            # Business Logic ของระบบ
│   ├── core/           # Infrastructure & Configuration
│   ├── scripts/        # สคริปต์สำหรับจัดการระบบ
│   └── utils/          # เครื่องมือและ Utilities ทั่วไป
├── infrastructure/     # (ถ้ามี) การตั้งค่า Docker และระบบอื่นๆ
├── README.md           # ไฟล์อธิบายโปรเจกต์ (ไฟล์นี้)
└── docker-compose.yml  # ไฟล์กำหนด Container Services
```

## Getting Started (การเริ่มต้นใช้งาน)
### ข้อกำหนดเบื้องต้น (Prerequisites)
- Docker และ Docker Compose
- Python 3.10+ และ `uv` package manager

### การติดตั้งและรันระบบ
1. **รัน Infrastructure Services:**
   ```bash
   docker compose up -d
   ```
2. **รัน Backend:**
   ```bash
   cd backend
   uv sync
   uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Documentation
เมื่อระบบรันสำเร็จ สามารถเข้าดูเอกสาร API ได้ที่:
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI JSON:** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## เครื่องมืออื่นๆ
- **Export API to CSV:** สำหรับนำข้อมูล API ออกมาในรูปแบบ CSV
  ```bash
  uv run python scripts/openapi_to_csv.py
  ```
