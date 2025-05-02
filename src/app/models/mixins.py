from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class IdPkMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


class PackIdMixin:
    pack_id: Mapped[int | None] = mapped_column(ForeignKey("packs.id"), nullable=True)
