from app.core.logging import setup_logging
from fastapi import FastAPI
from app.api.user_routes import router as user_router
from app.core.exceptions import AppException, app_exception_handler

app = FastAPI(title="Enterprise Python Service")

app.add_exception_handler(AppException, app_exception_handler)

@app.get("/")
async def root():
    return {"message": "Service is running successfully"}

app.include_router(user_router)

