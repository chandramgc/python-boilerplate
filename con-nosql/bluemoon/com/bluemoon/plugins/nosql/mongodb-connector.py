from pymongo import MongoClient
import os
import configparser
from constants import CONFIG_FILE_NAME

# Connect to mongodb and perform operations

class MongoDBConnector:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONFIG_FILE_NAME)

        database = config.get('MongoDB', 'MONGODB_DATABASE')
        host = config.get('MongoDB', 'MONGODB_HOST')
        port = config.get('MongoDB', 'MONGODB_PORT')
        username = os.environ.get("UNAME")
        password = os.environ.get("PNAME")

        connection_string = f"mongodb://{username}:{password}@{host}:{port}/{database}"
        self.client = MongoClient(connection_string)
        self.db = self.client.get_database()

    def insert_document(self, collection_name, document):
        collection = self.db.get_collection(collection_name)
        collection.insert_one(document)

    def find_documents(self, collection_name, query):
        collection = self.db.get_collection(collection_name)
        return collection.find(query)

    def update_document(self, collection_name, query, update):
        collection = self.db.get_collection(collection_name)
        collection.update_many(query, update)

    def delete_documents(self, collection_name, query):
        collection = self.db.get_collection(collection_name)
        collection.delete_many(query)

# Usage example
connector = MongoDBConnector()

print(connector)
