# Imports
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
# Custom Imports
from project.config import settings
from project.data.modelbase import SqlAlchemyBase

__async_engine: Optional[AsyncEngine] = None


async def global_init():
    global __async_engine

    if __async_engine:
        return

    async_conn_str = settings.DATABASE_URL
    __async_engine = create_async_engine(async_conn_str, connect_args=settings.DATABASE_CONNECT_DICT,
                                         echo=True, future=True)

    # noinspection PyUnresolvedReferences
    import project.data.__all_models

    # Create Tables from Models
    async with __async_engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.create_all)


def create_session() -> AsyncSession:
    global __async_engine

    if not __async_engine:
        raise Exception("You must call global_init() before using this method")

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False

    return session
