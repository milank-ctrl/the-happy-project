from pymongo.mongo_client import MongoClient
import certifi
from dotenv import load_dotenv
import os

load_dotenv()

class MongoManger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoManger, cls).__new__(cls)
            cls._instance.client = MongoClient(
                os.getenv("MONGO_URI"), tlsCAFile=certifi.where()
            )
        return cls._instance

    def insert_data(self, db_name: str, collection_name: str, data: list):
        """Insert multiple documents into a specified MongoDB database and collection."""
        if not data:
            print("No data to insert.")
            return

        db = self.client[db_name]  # Use dynamic database name
        collection = db[collection_name]

        try:
            result = collection.insert_many(data)
            print(f"Inserted {len(result.inserted_ids)} documents into {db_name}.{collection_name}.")
        except Exception as e:
            print(f"MongoDB insert failed: {str(e)}")

    def read_data(self, db_name: str, collection_name: str, filter_query=None):
        """Read documents from a specified MongoDB database and collection with optional filtering."""
        if filter_query is None:
            filter_query = {}
        db = self.client[db_name]  # Use dynamic database name
        collection = db[collection_name]

        try:
            documents = list(collection.find(filter_query))
            print(f"Retrieved {len(documents)} documents from {db_name}.{collection_name}.")
            return documents
        except Exception as e:
            print(f"MongoDB read failed: {str(e)}")
            return []


