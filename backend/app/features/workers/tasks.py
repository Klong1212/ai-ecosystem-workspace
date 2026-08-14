"""
Workers Tasks — ARQ task functions สำหรับ background jobs

เพิ่ม task functions ที่ต้องการรันเป็น background job ไว้ที่นี่
แล้ว register ใน WorkerSettings.functions

ตัวอย่างการเพิ่ม task:

    async def train_model(ctx, model_config: dict) -> str:
        # logic จริงใส่ตรงนี้
        return "training complete"

    class WorkerSettings:
        functions = [train_model]
        redis_settings = get_arq_redis_settings()

รัน worker:
    cd backend
    arq app.features.workers.tasks.WorkerSettings
"""

from core.redis_client import get_arq_redis_settings


class WorkerSettings:
    """
    ARQ Worker Settings

    รัน worker ด้วย:
        cd backend
        arq app.features.workers.tasks.WorkerSettings
    """

    functions = []
    redis_settings = get_arq_redis_settings()
