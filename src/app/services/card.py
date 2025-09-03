from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.models.card import TranslationCard, IrregularVerbCard
from app.services.base import BaseService
from app.schemas.card import (
    TranslationCardCreate,
    IrregularVerbCardCreate,
)
from app.schemas.progress import ProgressRead
from app.utils import db_helper


class CardService(BaseService):

    async def create_translation_card(
        self, data: TranslationCardCreate
    ) -> TranslationCard:
        card = TranslationCard(**data.model_dump())
        self.session.add(card)
        await self.session.commit()
        return card

    async def create_irregular_verb_card(
        self, data: IrregularVerbCardCreate
    ) -> IrregularVerbCard:
        card = IrregularVerbCard(**data.model_dump())
        self.session.add(card)
        await self.session.commit()
        return card

    async def get_translation_card_by_id(self, card_id: int) -> TranslationCard | None:
        return await self.session.get(TranslationCard, card_id)

    async def get_irregular_verb_card_by_id(
        self, card_id: int
    ) -> IrregularVerbCard | None:
        return await self.session.get(IrregularVerbCard, card_id)

    async def get_irregular_verb_cards_by_pack_id(
        self, pack_id: int
    ) -> list[IrregularVerbCard]:
        stmt = select(IrregularVerbCard).where(IrregularVerbCard.pack_id == pack_id)
        cards = await self.session.scalars(stmt)
        return list(cards)

    async def add_card_to_progress(
        self, user_id: int, data: TranslationCardCreate
    ) -> ProgressRead:

        stmt = select(TranslationCard).where(
            TranslationCard.original == data.original,
            TranslationCard.translated == data.translated,
        )

        card = await self.session.scalar(stmt)

        if card:
            ...


def get_card_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> CardService:
    """
    Возвращает экземпляр CardService с переданной сессией.
    """
    return CardService(session=session)
