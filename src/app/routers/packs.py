from typing import Annotated

from fastapi import APIRouter, status, Depends

from app.controllers.packs_controllers import get_cards
from app.models import IrregularVerbCard
from app.schemas.card import (
    IrregularVerbCardRead,
)
from app.schemas.pack import PackCreate, PackRead
from app.services import PackService, get_pack_service
from app.utils import settings

router = APIRouter(
    tags=["Packs"],
    prefix=settings.api.packs_prefix,
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=PackRead,
)
async def create_pack(
    request: PackCreate,
    pack_service: Annotated[PackService, get_pack_service],
):
    return pack_service.create_pack(
        name=request.name,
        description=request.description,
        card_type=request.card_type,
    )


@router.get(
    "/{pack_id}/cards/",
    status_code=status.HTTP_200_OK,
    response_model=list[
        IrregularVerbCardRead
    ],  # В дальнейшем добавить другие типы карт
)
async def get_cards_by_pack(
    cards: Annotated[list[IrregularVerbCard], Depends(get_cards)],
):
    return cards
