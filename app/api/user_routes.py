from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.dependencies import get_db_session
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user_api(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db_session)
):
    return await create_user(db, payload)

@router.get("/", response_model=List[UserResponse])
async def list_users_api(
    db: AsyncSession = Depends(get_db_session)
):
    return await get_users(db)
