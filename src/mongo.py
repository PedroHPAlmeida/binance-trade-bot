import os
from typing import Any, Dict, List, overload

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Mongo:
    def __init__(self, database: str, collection: str) -> None:
        self._client = MongoClient(os.getenv('MONGO_CONNECT_STRING'), server_api=ServerApi('1'))
        self._database_name = database
        self._collection_name = collection
        self._collection = self._client.get_database(self._database_name).get_collection(self._collection_name)

    def ping(self) -> None:
        try:
            self._client.admin.command('ping')
            print('Pinged your deployment. You successfully connected to MongoDB!')
        except Exception as e:
            print(e)

    @overload
    def save(self, documents: Dict[str, Any]) -> None:
        ...

    @overload
    def save(self, documents: List[Dict[str, Any]]) -> None:
        ...

    def save(self, documents: Dict[str, Any] | List[Dict[str, Any]]) -> None:
        if isinstance(documents, list):
            self._collection.insert_many(documents)
        else:
            self._collection.insert_one(documents)

    def find_all(self) -> List[Dict[str, Any]]:
        return [document for document in self._collection.find()]
