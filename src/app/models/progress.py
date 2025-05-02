from datetime import datetime

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import IdPkMixin


class Progress(IdPkMixin, Base):

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    card_id: Mapped[int] = mapped_column(
        ForeignKey("translation_cards.id"), primary_key=True
    )
    interval: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_shown: Mapped[datetime]
