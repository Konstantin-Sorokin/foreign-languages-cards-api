from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.card import TranslationCard


class Progress(Base):

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    card_id: Mapped[int] = mapped_column(
        ForeignKey("translation_cards.id"), primary_key=True
    )
    interval: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    last_shown: Mapped[datetime]

    card: Mapped["TranslationCard"] = relationship("TranslationCard")
