import os

from dotenv import load_dotenv
from pymongo.collection import Collection
from pymongo.mongo_client import MongoClient, database
from pymongo.server_api import ServerApi

load_dotenv()
MONGODB_PASSWORD = os.getenv(key="MONGODB_PASSWORD")
uri = f"mongodb+srv://subratasubha2:{MONGODB_PASSWORD}@fastapi-mongodb.aee8g.mongodb.net/?retryWrites=true&w=majority&appName=fastapi-mongodb"

# Create a new client and connect to the server
client: MongoClient = MongoClient(host=uri, server_api=ServerApi(version="1"))

db: database.Database = client.todo_db
collection: Collection = db["todo_data"]
    