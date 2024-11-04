from typing import Any, Generator, List

from fastapi import Depends, FastAPI
from sqlalchemy.orm.session import Session

from .database import PydanticUser, SessionLocal, SQLAlchemyUser

"""
This module sets up a FastAPI application with a single endpoint to read users from a database.
It uses SQLAlchemy for ORM and includes dependency injection for database sessions.
"""


# Dependency function to get a database session
def get_db() -> Generator[Session, Any, None]:
    """
    Dependency function to get a database session.

    Yields a database session after creating one using the SessionLocal factory.
    Closes the database session when the generator is exited (e.g. when the request is finished).
    """
    db: Session = SessionLocal()
    try:
        yield db
        print("Database session created...")
    finally:
        db.close()
        print("Database session closed...")


# Create an instance of the FastAPI application
app: FastAPI = FastAPI()


# Endpoint to read all users from the database
@app.get(path="/users/", response_model=List[PydanticUser])
def read_users(db: Session = Depends(dependency=get_db)) -> List[SQLAlchemyUser]:
    """
    Endpoint to read all users from the database.

    Returns:
        List[User]: List of all users in the database.
    """
    users: List[SQLAlchemyUser] = db.query(SQLAlchemyUser).all()
    return users


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True)
