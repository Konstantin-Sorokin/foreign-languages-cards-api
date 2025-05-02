from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.mixins import IdPkMixin


class Pack(IdPkMixin, Base):

    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(255))
    card_type: Mapped[str] = mapped_column(String(30))
