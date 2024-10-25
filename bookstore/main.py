from fastapi import FastAPI

app: FastAPI = FastAPI()


@app.get(path="/books/{book_id}")
async def read_book(book_id: int) -> dict[str, int | str]:
    if book_id == 44:
        return {
            "book_id": book_id,
            "title": "The Lord of the Rings",
            "author": "J.R.R. Tolkien",
        }
    else:
        return {"error": "Book not found"}


@app.get(path="/authors/{author_id}")
async def read_author(author_id: int) -> dict[str, int | str]:
    if author_id == 44:
        return {
            "author_id": author_id,
            "first_name": "J.R.R.",
            "last_name": "Tolkien",
        }
    else:
        return {"error": "Author not found"}
