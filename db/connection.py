from pymodm.connection import connect
from pymongo import MongoClient

from config import MONGO_DB_ALIAS, MONGO_DB_NAME, MONGO_HOST, MONGO_CONNECT


class Connection:
    def create_connection(self):
        is_db_exist = self._check_db()
        self._connect()
        return is_db_exist

    @staticmethod
    def _connect():
        connect(MONGO_CONNECT, alias=MONGO_DB_ALIAS)

    @staticmethod
    def _check_db():
        if MONGO_DB_NAME in MongoClient(MONGO_HOST).list_database_names():
            return True
        else:
            return False
