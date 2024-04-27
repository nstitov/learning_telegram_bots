import asyncio

from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class GameHistoryEntry(Base):
    __tablename__ = "gameshistory"

    game_id = Column(UUID, primary_key=True)
    played_at = Column(DateTime, nullable=False)
    telegram_id = Column(BigInteger, nullable=False, index=True)
    field_size = Column(Integer, nullable=False)
    victory = Column(Boolean, nullable=False)


async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://nstitov@localhost/testdb", echo=True
    )
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(async_main())
