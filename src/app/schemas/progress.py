from datetime import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.schemas.card import TranslationCardRead


class ProgressCreate(BaseModel):
    interval: int
    last_shown: datetime


class ProgressUpdate(BaseModel):
    interval: int
    last_shown: datetime


class ProgressRead(BaseModel):
    interval: int
    last_shown: datetime
    card: "TranslationCardRead"
