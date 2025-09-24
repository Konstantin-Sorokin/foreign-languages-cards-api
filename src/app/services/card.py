from sqlalchemy import select

from app.models import TranslationCard, IrregularVerbCard
from app.services.base import BaseService


class CardService(BaseService):

    async def create_irregular_verb_card(
        self,
        base_form: str,
        past_simple: str,
        past_participle: str,
        translation: str,
        pack_id: int,
    ) -> IrregularVerbCard:
        card = IrregularVerbCard(
            base_form=base_form,
            past_simple=past_simple,
            past_participle=past_participle,
            translation=translation,
            pack_id=pack_id,
        )
        self.session.add(card)
        await self.session.commit()
        return card

    async def get_irregular_verb_cards_by_pack_id(
        self, pack_id: int
    ) -> list[IrregularVerbCard]:
        stmt = select(IrregularVerbCard).where(IrregularVerbCard.pack_id == pack_id)
        cards = await self.session.scalars(stmt)
        return list(cards)

    async def get_or_create_card(
        self, original: str, translation: str
    ) -> TranslationCard:
        stmt = select(TranslationCard).where(
            TranslationCard.original == original,
            TranslationCard.translation == translation,
        )
        card = await self.session.scalar(stmt)
        if card:
            return card

        card = TranslationCard(original=original, translation=translation)
        self.session.add(card)
        await self.session.flush()
        return card
