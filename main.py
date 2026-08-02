from fastapi import FastAPI

from routers.student import router as student_router

app = FastAPI(
    title="College Management API"
)

app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)