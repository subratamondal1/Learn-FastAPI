from fastapi import FastAPI

from . import router_example

app: FastAPI = FastAPI()
app.include_router(router=router_example.router)


@app.get(path="/")
def read_root() -> dict[str, str]:
    return {"Hello": "World"}
