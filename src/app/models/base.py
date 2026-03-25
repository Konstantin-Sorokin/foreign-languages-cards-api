from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from app.utils import settings
from app.utils.case_converter import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(
        naming_convention=settings.db.naming_convention,
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        name = camel_case_to_snake_case(cls.__name__)
        return name if name.endswith("s") else f"{name}s"
