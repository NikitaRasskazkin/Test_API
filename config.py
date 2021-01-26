import os

environ_get = os.environ.get
DB_CONNECT = environ_get('DB_CONNECT')
DB_NAME = environ_get('DB_NAME')
if not(DB_CONNECT and DB_NAME):
    DB_CONNECT = "mongodb://localhost:27017/Currencies"
    DB_NAME = "Currencies"
