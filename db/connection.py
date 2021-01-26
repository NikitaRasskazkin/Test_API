from pymodm.connection import connect
from pymongo import MongoClient

from config import DB_CONNECT, DB_NAME


class Connection:
    def __init__(self):
        self.connection_string = DB_CONNECT
        self.db_name = DB_NAME

    def create_connection(self, alias: str = 'main'):
        is_db_exist = self._check_db()
        connect(self.connection_string, alias=alias)
        return not is_db_exist

    def _check_db(self):
        if self.db_name in MongoClient(self.connection_string).list_database_names():
            return True
        else:
            return False
