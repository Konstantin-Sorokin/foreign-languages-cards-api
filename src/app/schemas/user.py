from pydantic import BaseModel


class UserCreate(BaseModel):
    first_name: str
    last_name: str | None
    username: str | None


class UserUpdate(BaseModel):
    first_name: str | None
    last_name: str | None
    username: str | None


class UserRead(BaseModel):
    first_name: str
    last_name: str | None
    username: str | None
