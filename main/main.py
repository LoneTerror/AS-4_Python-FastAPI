from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.prisma import db #DB instance created in app/db/prisma.py

@asynccontextmanager
async def lifespan(app: FastAPI):
    #STARTING THE DATABASE FIRST FOR THE APPLICATION TO USE
    print("Connecting to Database...")
    await db.connect()
    print("Database Connected!")
    yield # The application runs here
    
    # --- SHUTDOWN ---
    print("Disconnecting from Database...")
    if db.is_connected():
        await db.disconnect()

# Register the lifespan events
app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    # NOW USE DB ANYWHERE IN THE APPLICATION
    return {"message": "API is online and DB is connected"}