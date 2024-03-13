import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Mongo:
    def __init__(self) -> None:
        self._client = MongoClient(os.getenv('MONGO_CONNECT_STRING'), server_api=ServerApi('1'))

    def ping(self) -> None:
        try:
            self._client.admin.command('ping')
            print('Pinged your deployment. You successfully connected to MongoDB!')
        except Exception as e:
            print(e)
