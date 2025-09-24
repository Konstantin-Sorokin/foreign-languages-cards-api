from typing import Annotated

from fastapi import Path, Depends, HTTPException

from app.models import Pack, IrregularVerbCard
from app.services import (
    CardService,
    PackService,
    get_card_service,
    get_pack_service,
)
from app.utils.card_types import IRREGULAR_VERB_CARD


async def get_cards(
    pack_id: Annotated[int, Path()],
    card_service: Annotated[CardService, Depends(get_card_service)],
    pack_service: Annotated[PackService, Depends(get_pack_service)],
) -> list[IrregularVerbCard]:

    pack: Pack = await pack_service.get_pack_by_id(pack_id=pack_id)

    if pack.card_type == IRREGULAR_VERB_CARD:
        return await card_service.get_irregular_verb_cards_by_pack_id(pack_id=pack_id)

    raise HTTPException(
        status_code=400, detail=f"Не поддерживаемый тип карт {pack.card_type}"
    )
