from fastapi import FastAPI
from app.routes import age_group, enrollment
import asyncio
from app.database import init_db
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init_db()
#inclusão das rotas
app.include_router(age_group.router)
app.include_router(enrollment.router)