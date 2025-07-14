from fastapi import FastAPI
from src.routers import wheel_sepecification

app = FastAPI()

app.include_router(wheel_sepecification.router)

from src.database import models
from src.database.connect import engine
models.Base.metadata.create_all(bind=engine)