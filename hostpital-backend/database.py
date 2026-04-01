# database.py — MongoDB Motor async client
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorGridFSBucket
from config import MONGO_URI, DB_NAME

# Global references
_client: AsyncIOMotorClient = None
_db = None
_fs: AsyncIOMotorGridFSBucket = None


async def connect_db():
    global _client, _db, _fs
    _client = AsyncIOMotorClient(MONGO_URI)
    _db = _client[DB_NAME]
    _fs = AsyncIOMotorGridFSBucket(_db)
    # Create indexes
    await _db.patients.create_index("patient_id", unique=True)
    await _db.vitals.create_index([("patient_id", 1), ("recorded_at", -1)])
    await _db.alerts.create_index([("target_role", 1), ("acknowledged", 1)])
    print(f"Connected to MongoDB: {DB_NAME}")


async def close_db():
    global _client
    if _client:
        _client.close()
        print("MongoDB connection closed")


def get_db():
    return _db


def get_fs() -> AsyncIOMotorGridFSBucket:
    return _fs
