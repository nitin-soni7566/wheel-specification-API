from fastapi import FastAPI
from src.database import models
from src.database.connect import engine
from src.routers import wheel_sepecification
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


models.Base.metadata.create_all(bind=engine)

app.include_router(wheel_sepecification.router)
