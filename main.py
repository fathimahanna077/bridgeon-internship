from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from database import init_db

from routers.auth_routes import router as auth_router
from routers.tasks import router as task_router

app = FastAPI()


@app.on_event("startup")
def startup():

    init_db()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(task_router)


@app.get("/")
def home():

    return {
        "message": "Secure Task API"
    }