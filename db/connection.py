from pymodm.connection import connect
from pymongo import MongoClient

from config import DB_CONNECT, DB_NAME


class Connection:
    def create_connection(self, alias: str):
        is_db_exist = self._check_db()
        connect(DB_CONNECT, alias=alias)
        return is_db_exist

    @staticmethod
    def _check_db():
        if DB_NAME in MongoClient(DB_CONNECT).list_database_names():
            return True
        else:
            return False
