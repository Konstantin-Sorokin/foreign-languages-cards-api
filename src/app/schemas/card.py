from pydantic import BaseModel


class TranslationCardCreate(BaseModel):
    original: str
    translation: str
    pack_id: int | None


class TranslationCardRead(BaseModel):
    id: int
    original: str
    translation: str


class IrregularVerbCardCreate(BaseModel):
    base_form: str
    past_simple: str
    past_participle: str
    translation: str
    pack_id: int


class IrregularVerbCardRead(BaseModel):
    id: int
    base_form: str
    past_simple: str
    past_participle: str
    translation: str
