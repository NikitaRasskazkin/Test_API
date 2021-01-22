from os.path import dirname, isfile, join
from dotenv import load_dotenv
import os

DIR_PATH = dirname(__file__)
ENV_PATH = join(DIR_PATH, '.env')

if not isfile(ENV_PATH):
    raise FileNotFoundError('.env not found')

load_dotenv(ENV_PATH)
environ_get = os.environ.get


MONGO_PORT = int(environ_get('MONGO_PORT'))
MONGO_DB_NAME = environ_get('MONGO_DB_NAME')
MONGO_DB_ALIAS = environ_get('MONGO_DB_ALIAS')
MONGO_HOST = environ_get('MONGO_HOST')
MONGO_CONNECT = MONGO_HOST + MONGO_DB_NAME
