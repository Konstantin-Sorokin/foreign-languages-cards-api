from fastapi import APIRouter

from app.routers.cards import router as card_router
from app.routers.packs import router as pack_router
from app.routers.users import router as user_router
from app.utils import settings

router = APIRouter(prefix=settings.api.prefix)

router.include_router(card_router)
router.include_router(pack_router)
router.include_router(user_router)
