from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user_schema import UserCreate

async def create_user(db: AsyncSession, data: UserCreate):
    user = User(email=data.email, name=data.name)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
