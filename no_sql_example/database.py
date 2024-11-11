from typing import List

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

# Create a MongoDB client
client = MongoClient()

# Connect to the "subrata" database
database: Database = client.subrata  # "subrata" is the database name

user_collection: Collection = database.users  # "users" is the collection name

# List the names of all collections(tables) in the "subrata" database
collection_names: List[str] = database.list_collection_names()
print(collection_names)

# Insert a document(row) into the "users" collection(tables)
user_collection.insert_one(document={"name": "John Doe", "age": 30})

# Find a document(row) in the "users" collection(tables)
user = user_collection.find_one(filter={"name": "John Doe"})
print(user)
