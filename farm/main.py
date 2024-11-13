from typing import Union

from fastapi import FastAPI

from .schema import Item

app: FastAPI = FastAPI()


@app.get(path="/")
async def read_root() -> dict[str, Union[str, int]]:
    return {"message": "Hello World"}


@app.get(path="/items/{item_id}")
async def read_item(
    item_id: int, q: Union[str, None] = None
) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}


@app.put(path="/items/{item_id}")
async def update_item(item_id: int, item: Item) -> dict[str, int | str | None]:
    return {"item_name": item.name, "item_id": item_id}
