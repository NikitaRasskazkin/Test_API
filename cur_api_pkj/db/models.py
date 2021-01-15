from pymodm import MongoModel, fields
from pymodm.connection import connect
from pymongo.write_concern import WriteConcern
import json

from cur_api_pkj.db.queryset import manager


connect('mongodb://localhost:27017/projectDB2', alias="my-app")


class Currencies(MongoModel):
    name = fields.CharField()
    value = fields.FloatField()
    objects = manager()

    class Meta:
        write_concern = WriteConcern(j=True)
        connection_alias = 'my-app'
        final = True


if __name__ == '__main__':
    with open('data/currencies.json', encoding='utf-8') as file:
        currencies = [
            Currencies(name=key, value=value)
            for key, value in dict(json.load(file)).items()
        ]
        Currencies.objects.bulk_create(currencies)
        print('Data base is created')
