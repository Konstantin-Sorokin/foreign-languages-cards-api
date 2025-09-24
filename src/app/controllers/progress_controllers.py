from typing import Annotated

from fastapi import Path, Depends, HTTPException, status

from app.schemas.card import TranslationCardCreate
from app.services import (
    CardService,
    ProgressService,
    get_card_service,
    get_progress_service,
)


async def create_progress(
    user_id: Annotated[int, Path()],
    card_service: Annotated[CardService, Depends(get_card_service)],
    progress_service: Annotated[ProgressService, Depends(get_progress_service)],
    request: TranslationCardCreate,
) -> int:

    session = card_service.session

    try:
        async with session.begin():
            card = await card_service.get_or_create_card(
                request.original, request.translation
            )
            await progress_service.create_progress(user_id, card.id)
        return card.id

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Не удалось сохранить данные. Попробуйте позже.",
        )
