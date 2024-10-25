from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get(path="/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}
