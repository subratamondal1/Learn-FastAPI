from typing import Any, Generator, List

from database import SessionLocal, User
from fastapi import Depends, FastAPI
from sqlalchemy.orm.session import Session

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
    finally:
        db.close()


# Create an instance of the FastAPI application
app: FastAPI = FastAPI()


# Endpoint to read all users from the database
@app.get(path="/users/")
def read_users(db: Session = Depends(dependency=get_db)) -> List[User]:
    """
    Endpoint to read all users from the database.

    Returns:
        List[User]: List of all users in the database.
    """
    users: List[User] = db.query(_entity=User).all()
    return users
