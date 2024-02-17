from pydantic import BaseModel, ConfigDict


class SWordAdd(BaseModel):
    word: str
    translate: str


class SWord(SWordAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SWordId(BaseModel):
    id: int
