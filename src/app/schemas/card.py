from pydantic import BaseModel


class TranslationCardCreate(BaseModel):
    original: str
    translated: str
    pack_id: int | None


class TranslationCardRead(BaseModel):
    id: int
    original: str
    translated: str


class IrregularVerbCardCreate(BaseModel):
    base_form: str
    past_simple: str
    past_participle: str
    translated: str
    pack_id: int


class IrregularVerbCardRead(BaseModel):
    id: int
    base_form: str
    past_simple: str
    past_participle: str
    translated: str
