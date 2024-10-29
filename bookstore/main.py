from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .routers import authors, books

app: FastAPI = FastAPI()
app.include_router(router=books.router)
app.include_router(router=authors.router)


@app.exception_handler(exc_class_or_status_code=HTTPException)
async def custom_exception_handler(request, exc) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "message": "Oops! Something went wrong."},
    )


@app.get(path="/")
async def read_root() -> dict[str, str]:
    return {"data": "Welcome to Bookstore!"}


@app.get(path="/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)
