from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

"""
This module sets up the SQLAlchemy ORM and database connection for the application.
It defines the base class for models, the User model, and initializes the database connection.
"""


# Define a declarative base class for all ORM models
class Base(DeclarativeBase):
    pass


# Define the User model with columns id, name, and email
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]


# Database connection string for SQLite database
DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine using the connection string
engine: Engine = create_engine(url=DATABASE_URL)

# Create tables in the database based on the defined models
Base.metadata.create_all(bind=engine)

# Create a session factory for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
