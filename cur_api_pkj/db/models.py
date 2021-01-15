from pymodm import MongoModel, fields
from pymongo.write_concern import WriteConcern
import json
import os

from cur_api_pkj.db.connection import Connection
from cur_api_pkj.db.queryset import manager
from cur_api_pkj.config import db_alias


class Currencies(MongoModel):
    name = fields.CharField()
    value = fields.FloatField()
    objects = manager()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = db_alias
        final = True


connect = Connection()
is_db_ready = connect.create_connection()
if not is_db_ready:
    with open(f'{os.path.abspath(__file__)[:-9]}\\data\\currencies.json', encoding='utf-8') as file:
        currencies = [
            Currencies(name=key, value=value)
            for key, value in dict(json.load(file)).items()
        ]
        Currencies.objects.bulk_create(currencies)
        print('Data base is created')


if __name__ == '__main__':
    pass
