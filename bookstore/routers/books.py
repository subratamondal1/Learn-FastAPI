from fastapi import APIRouter

from ..models import Book, BookResponse

router: APIRouter = APIRouter()


@router.get(path="/books/{book_id}")
async def read_book(book_id: int) -> dict[str, int | str]:
    if book_id == 44:
        return {
            "book_id": book_id,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
        }
    else:
        return {"error": "Book not found"}


@router.post(path="/book")
async def create_book(book: Book) -> Book:
    print(book.model_dump_json())
    return book


@router.get(path="/books")
async def read_books(year: int | None = None) -> dict[str, int | str | list]:
    if year:
        return {"year": year, "books": ["Book1", "Book 2"]}
    return {"books": ["All Books"]}


@router.get(path="/allbooks")
async def read_all_books() -> list[BookResponse]:
    return [
        BookResponse(title="Book1", author="Author1"),
        BookResponse(title="Book2", author="Author2"),
    ]
