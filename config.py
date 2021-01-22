from os.path import dirname, isfile, join
from dotenv import load_dotenv
import os
#
# DIR_PATH = dirname(__file__)
# ENV_PATH = join(DIR_PATH, '.env')
#
# if not isfile(ENV_PATH):
#     raise FileNotFoundError('.env not found')
#
# load_dotenv(ENV_PATH)
environ_get = os.environ.get


DB_CONNECT = environ_get('DB_CONNECT')
DB_NAME = environ_get('DB_NAME')
