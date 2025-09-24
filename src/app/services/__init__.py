from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.card import CardService
from app.services.pack import PackService
from app.services.progress import ProgressService
from app.utils import db_helper


def get_card_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> CardService:
    """
    Возвращает экземпляр CardService с переданной сессией.
    """
    return CardService(session=session)


def get_progress_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> ProgressService:
    """
    Возвращает экземпляр ProgressService с переданной сессией.
    """
    return ProgressService(session=session)


def get_pack_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> PackService:
    """
    Возвращает экземпляр PackService с переданной сессией.
    """
    return PackService(session=session)
