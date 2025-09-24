from typing import Annotated

from fastapi import APIRouter, status, Depends, Path

from app.controllers.progress_controllers import create_progress
from app.schemas.progress import ProgressRead, ProgressUpdate
from app.services import ProgressService, get_progress_service
from app.utils import settings

router = APIRouter(
    tags=["Users"],
    prefix=settings.api.users_prefix,
)


@router.post("/{user_id}/progress/", status_code=status.HTTP_201_CREATED)
async def create_progress_for_user(
    card_id: Annotated[int, Depends(create_progress)],
) -> int:
    return card_id


@router.get(
    "/{user_id}/progress/",
    response_model=list[ProgressRead],
    status_code=status.HTTP_200_OK,
)
async def get_all_need_progress_for_user(
    user_id: Annotated[int, Path()],
    progress_service: Annotated[ProgressService, Depends(get_progress_service)],
):
    return await progress_service.get_all_need_progress(user_id)


@router.patch("/{user_id}/card/{card_id}/progress/", status_code=status.HTTP_200_OK)
async def update_progress_card_for_user(
    user_id: Annotated[int, Path(description="ID пользователя")],
    card_id: Annotated[int, Path(description="ID карточки")],
    request: ProgressUpdate,
    progress_service: Annotated[ProgressService, Depends(get_progress_service)],
):

    return await progress_service.update_progress(
        user_id=user_id,
        card_id=card_id,
        success=request.success,
    )
