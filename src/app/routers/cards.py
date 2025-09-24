from typing import Annotated

from fastapi import APIRouter, status, Depends

from app.schemas.card import (
    IrregularVerbCardCreate,
    IrregularVerbCardRead,
)
from app.services import CardService, get_card_service
from app.utils import settings

router = APIRouter(
    tags=["Cards"],
    prefix=settings.api.cards_prefix,
)


@router.post(
    "/iv-card/",
    status_code=status.HTTP_201_CREATED,
    response_model=IrregularVerbCardRead,
)
async def create_irregular_verb_card(
    request: IrregularVerbCardCreate,
    card_service: Annotated[CardService, Depends(get_card_service)],
):
    return await card_service.create_irregular_verb_card(**request.model_dump())
