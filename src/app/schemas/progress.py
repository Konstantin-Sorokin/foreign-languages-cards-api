from pydantic import BaseModel

from app.schemas.card import TranslationCardRead


class ProgressRead(BaseModel):
    interval: int
    card: TranslationCardRead


class ProgressUpdate(BaseModel):
    success: bool
