import enum

from fastapi import APIRouter

router: APIRouter = APIRouter()


class BookType(enum.Enum):
    one: str = "subrata"
    two: str = "mondal"


@router.get(path="/books/{book_id}")
async def read_book(book_id: BookType) -> dict[str, int | str]:
    if book_id == 44:
        return {
            "book_id": book_id,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
        }
    else:
        return {"error": "Book not found"}


@router.get(path="/books")
async def read_books(year: int | None = None) -> dict[str, int | str | list]:
    if year:
        return {"year": year, "books": ["Book1", "Book 2"]}
    return {"books": ["All Books"]}
