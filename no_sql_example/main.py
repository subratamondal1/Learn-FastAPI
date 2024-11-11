from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo.results import InsertOneResult

from .database import user_collection

app: FastAPI = FastAPI()


class User(BaseModel):
    name: str
    email: str


@app.get(path="/")
async def home() -> dict[str, str]:
    return {"Welcome": "Mongo DB"}


@app.get(path="/users")
async def read_users():
    users = list(user_collection.find())
    # Convert ObjectId to string for each user
    for user in users:
        user["_id"] = str(object=user["_id"])
    return {"users": users}


class UserResponse(User):
    id: str


@app.post(path="/user")
async def create_user(user: User) -> UserResponse:
    result: InsertOneResult = user_collection.insert_one(
        document=user.model_dump(exclude_none=True)
    )

    user_response = UserResponse(
        id=str(object=result.inserted_id),
        **user.model_dump(exclude_none=True),
    )
    return user_response


@app.get("/user")
async def get_user(user_id: str) -> UserResponse:
    db_user = user_collection.find_one(
        filter={"_id": ObjectId(user_id) if ObjectId.is_valid(user_id) else None}
    )

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_response = UserResponse(id=str(object=db_user["_id"]), **db_user)
    return user_response
