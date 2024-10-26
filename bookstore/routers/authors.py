from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get(path="/authors/{author_id}")
async def read_author(author_id: int) -> dict[str, int | str]:
    if author_id == 44:
        return {
            "author_id": author_id,
            "first_name": "J.R.R.",
            "last_name": "Tolkien",
        }
    else:
        return {"error": "Author not found"}
