from enum import Enum

from pydantic import BaseModel, Field


class BookGenre(Enum):
    fiction: str = "FICTION F"
    horror: str = "HORROR H"


class Book(BaseModel):
    title: str = Field(
        default=...,
        title="Book Title",
        description="The title of the book",
        max_length=100,
    )
    author: str = Field(
        default=...,
        title="Book Author",
        description="The author of the book",
        max_length=50,
    )
    year: int = Field(
        default=...,
        title="Book Year",
        description="The year the book was published",
        gt=0,
        lt=2024,
    )
    genre: BookGenre = Field(
        default=..., title="Book Genre", description="The genre of the book"
    )


class BookResponse(BaseModel):
    title: str
    author: str
