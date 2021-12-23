from sqlalchemy.future import select
from typing import Optional

from project.data import db_session
from project.data.users.user_model import User


async def find_user_by_username(username: str) -> Optional[User]:
    async with db_session.create_session() as session:
        query = select(User).filter(User.username == username)
        result = await session.execute(query)

        return result.scalar_one_or_none()


async def find_user_by_email(email: str) -> Optional[User]:
    async with db_session.create_session() as session:
        query = select(User).filter(User.email == email)
        result = await session.execute(query)

        return result.scalar_one_or_none()


async def create_user(username: str, email: str) -> Optional[User]:
    # Create User Object
    user = User(username=username, email=email)

    # Add user to database and commit
    async with db_session.create_session() as session:
        session.add(user)
        await session.commit()

    await session.close()

    return user
