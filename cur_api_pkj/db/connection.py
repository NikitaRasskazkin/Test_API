from pymodm.connection import connect
from pymongo import MongoClient
import json
import os

from cur_api_pkj.config import db_alias


class Connection:
    def __init__(self):
        db_config = self._open_config()
        self.name = db_config['name']
        self.port = db_config['port']

    def create_connection(self):
        if self.name:
            self._connect(self.name, self.port)
            return True
        else:
            self._setup_db()
            self._connect(self.name, self.port)
            self._write_config(self.name)
            return False

    @staticmethod
    def _connect(name, port):
        connect(f'mongodb://localhost:{port}/{name}', alias=db_alias)

    @staticmethod
    def _open_config():
        with open(f'{os.path.abspath(__file__)[:-13]}\\db_config.json', encoding='utf-8') as file:
            return json.load(file)

    def _setup_db(self):
        print('The database is not configured. Enter the name of the database:')
        self.name = input('name: ')
        client = MongoClient('localhost', self.port)
        db = client[self.name]

    def _write_config(self, name: str):
        with open(f'{os.path.abspath(__file__)[:-13]}\\db_config.json', 'w', encoding='utf-8') as file:
            new_db_config = {
                'name': name,
                'port': self.port
            }
            json.dump(new_db_config, file)
