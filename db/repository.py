from pymongo import MongoClient

from db.base import alias
from db.models import Currency
from db.connection import Connection
from db.insert_data import insert_all_models_data
from config import DB_CONNECT, DB_NAME


def init_database():
    connect = Connection()
    is_db_empty = connect.create_connection(alias)
    if is_db_empty:
        insert_all_models_data()


def drop_database():
    MongoClient(DB_CONNECT).drop_database(DB_NAME)


def get_currency_value(name: str):
    return Currency.objects.get_currency(name)


def update_currency(name: str, value: float):
    if get_currency_value(name) is not None:
        return Currency.objects.update_currencies(name, round(value, 10))
    else:
        return None


def get_converted_currency(from_currency: str, to_currency: str, from_quantity: float):
    from_value = Currency.objects.get_currency(from_currency)
    to_value = Currency.objects.get_currency(to_currency)
    if not from_value or not to_value:
        return None
    return round(to_value / from_value * from_quantity, 10)


if __name__ == '__main__':
    pass
