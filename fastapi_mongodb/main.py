import datetime
from datetime import datetime

from bson.objectid import ObjectId
from fastapi import APIRouter, FastAPI, HTTPException

from .config import collection
from .database.models import Todo
from .database.schemas import all_tasks

app: FastAPI = FastAPI()
router = APIRouter()


@router.get(path="/")
async def get_all_todos():
    data = collection.find()
    return all_tasks(todos=data)


@router.post(path="/")
async def create_task(new_task: Todo):
    try:
        res = collection.insert_one(dict(new_task))
        return {"status_code": 200, "id": str(object=res.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error: {e}")


@router.put(path="/{task_id}")
async def update_task(task_id: str, updated_task: Todo):
    try:
        id = ObjectId(oid=task_id)
        existing_doc = collection.find_one(filter={"_id": id, "is_deleted": False})
        if not existing_doc:
            return HTTPException(
                status_code=404, detail="Invalid Task Id:{id}, it does not exist"
            )
        updated_task.updated_at = int(datetime.timestamp(datetime.now()))
        res = collection.update_one(
            filter={"_id": id}, update={"$set": dict(updated_task)}
        )
        return {"status_code": 200, "message": "Task Updated Successfully"}
    except Exception as e:
        return HTTPException(status_code=404, detail=f"Error: {e}")


app.include_router(router=router)
