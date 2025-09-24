from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import IdPkMixin


class TranslationCard(IdPkMixin, Base):

    original: Mapped[str] = mapped_column(String(255))
    translation: Mapped[str] = mapped_column(String(255))
    pack_id: Mapped[int | None] = mapped_column(
        ForeignKey("packs.id"),
        nullable=True,
        index=True,
    )


class IrregularVerbCard(IdPkMixin, Base):

    base_form: Mapped[str] = mapped_column(String(30))
    past_simple: Mapped[str] = mapped_column(String(30))
    past_participle: Mapped[str] = mapped_column(String(30))
    translation: Mapped[str] = mapped_column(String(30))
    pack_id: Mapped[int] = mapped_column(
        ForeignKey("packs.id"),
        nullable=False,
        index=True,
    )
