from pymodm.connection import connect
from pymongo import MongoClient

from config import DB_CONNECT, DB_NAME, DEFAULT_DB_NAME, DEFAULT_DB_CONNECT


class Connection:
    def __init__(self):
        if DB_CONNECT and DB_NAME:
            self.connection_string = DB_CONNECT
            self.db_name = DB_NAME
        else:
            self.connection_string = DEFAULT_DB_CONNECT
            self.db_name = DEFAULT_DB_NAME

    def create_connection(self, alias: str):
        is_db_exist = self._check_db()
        connect(self.connection_string, alias=alias)
        return is_db_exist

    def _check_db(self):
        if self.db_name in MongoClient(self.connection_string).list_database_names():
            return True
        else:
            return False
