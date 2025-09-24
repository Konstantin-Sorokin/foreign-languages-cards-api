from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas.card import TranslationCardRead


class ProgressRead(BaseModel):
    interval: int
    card: "TranslationCardRead"


class ProgressUpdate(BaseModel):
    success: bool
