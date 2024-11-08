from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(
        __name_pos=Integer, primary_key=True, autoincrement=True
    )

    publication_date: Mapped[datetime] = mapped_column(
        __name_pos=DateTime, nullable=False, default=datetime.now
    )
    title: Mapped[str] = mapped_column(__name_pos=String(length=255), nullable=False)
    content: Mapped[str] = mapped_column(__name_pos=Text, nullable=False)
