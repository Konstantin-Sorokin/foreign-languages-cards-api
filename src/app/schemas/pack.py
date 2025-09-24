from pydantic import BaseModel

from app.utils.card_types import CardType


class PackCreate(BaseModel):
    name: str
    description: str
    card_type: CardType


class PackRead(BaseModel):
    id: int
    name: str
    description: str
    card_type: CardType
