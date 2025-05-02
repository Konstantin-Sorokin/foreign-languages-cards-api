from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import IdPkMixin, PackIdMixin


class TranslationCard(IdPkMixin, PackIdMixin, Base):

    original: Mapped[str] = mapped_column(String(255))
    translated: Mapped[str] = mapped_column(String(255))


class IrregularVerbCard(IdPkMixin, PackIdMixin, Base):

    base_form: Mapped[str] = mapped_column(String(30))
    past_simple: Mapped[str] = mapped_column(String(30))
    past_participle: Mapped[str] = mapped_column(String(30))
    translated: Mapped[str] = mapped_column(String(30))
