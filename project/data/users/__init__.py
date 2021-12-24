from fastapi import APIRouter

from project.services import user_service

users_router = APIRouter(
    prefix="/users",
)


@users_router.get("/")
async def get_username(username: str):
    username = await user_service.find_user_by_username(username)

    return username


@users_router.post("/")
async def create_user(username: str, email: str):
    user = await user_service.create_user(username, email)

    return user


from . import user_model, tasks
