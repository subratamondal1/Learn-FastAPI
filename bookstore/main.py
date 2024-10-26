from fastapi import FastAPI

from .routers import authors, books

app: FastAPI = FastAPI()
app.include_router(router=books.router)
app.include_router(router=authors.router)


@app.get(path="/")
async def read_root() -> dict[str, str]:
    return {"data": "Welcome to Bookstore!"}
