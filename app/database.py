import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client["enrollment_db"]


age_group_collection = database.get_collection("age_groups")
enrollment_collection = database.get_collection("enrollments")

async def init_db():
  await enrollment_collection.create_index("cpf", unique=True)