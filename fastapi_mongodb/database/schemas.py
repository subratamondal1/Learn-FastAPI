from typing import Any


def individual_data(todo) -> dict[str, Any]:
    return {
        "id": str(object=todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "status": todo["is_completed"],
    }


def all_tasks(todos) -> list[dict[str, Any]]:
    return [individual_data(todo=todo) for todo in todos]
