from db.base import Base
from sqlalchemy import BigInteger, Boolean, Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID


class GameHistoryEntry(Base):
    __tablename__ = "gamehistory"

    game_id = Column(UUID, primary_key=True)
    player_at = Column(DateTime, nullable=False)
    telegram_id = Column(BigInteger, nullable=False, index=True)
    field_size = Column(Integer, nullable=False)
    victory = Column(Boolean, nullable=False)
