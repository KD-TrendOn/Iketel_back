from db import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text
from datetime import datetime, UTC
from functools import partial


class User(Base):
    """
    class User:
    id int
    username str
    email str
    hashed_password str
    date_created datetime
    """
    __tablename__ = 'users'
    username : Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    disabled: Mapped[str] = mapped_column(nullable=True)
    date_created: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    def __repr__(self) -> str:
        return  f"<User {self.username} at {self.date_created}"
