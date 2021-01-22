import os

environ_get = os.environ.get
DEFAULT_DB_CONNECT = "mongodb://localhost:27017/Currencies"
DEFAULT_DB_NAME = "Currencies"
DB_CONNECT = environ_get('DB_CONNECT')
DB_NAME = environ_get('DB_NAME')
