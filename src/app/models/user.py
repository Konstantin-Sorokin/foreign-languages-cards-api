from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):

    telegram_id: Mapped[int | None] = mapped_column(
        Integer, unique=True, nullable=False
    )  # nullable=False, пока нет email и password
    # email: Mapped[str | None] = mapped_column(String(255), unique=True, nullable=True)
    # password: Mapped[str | None] = mapped_column(String(255), nullable=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str | None] = mapped_column(String(64), nullable=True)
    username: Mapped[str | None] = mapped_column(String(32), nullable=True)
