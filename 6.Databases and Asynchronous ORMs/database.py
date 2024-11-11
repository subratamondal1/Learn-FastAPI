from datetime import datetime
from typing import Any, Callable, Generator

from bson import ObjectId
from pydantic import BaseModel, Field


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., ObjectId], Any, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v) -> ObjectId:
        if not ObjectId.is_valid(oid=v):
            raise ValueError("Invalid objectid")
        return ObjectId(oid=v)

    @classmethod
    def __modify_schema__(cls, field_schema) -> None:
        field_schema.update(type="string")


class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders: dict[type[ObjectId], type[str]] = {ObjectId: str}


class PostBase(MongoBaseModel):
    title: str
    content: str
    publication_date: datetime = Field(default_factory=datetime.now)


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    pass
