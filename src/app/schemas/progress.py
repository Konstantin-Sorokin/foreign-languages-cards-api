from pydantic import BaseModel


class ProgressUpdate(BaseModel):
    success: bool
