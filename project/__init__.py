from fastapi import FastAPI
from project.data import db_session


def create_app() -> FastAPI:
    app = FastAPI()

    from project.data.users import users_router
    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello, World"}

    return app
