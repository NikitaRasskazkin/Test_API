from pymodm import MongoModel, fields
from pymodm.connection import connect
import json

from db.queryset import manager


connect('mongodb://localhost:27017/projectDB2')


class Currencies(MongoModel):
    name = fields.CharField(primary_key=True)
    value = fields.FloatField()
    objects = manager()


if __name__ == '__main__':
    # with open('data/currencies.json', encoding='utf-8') as file:
    #     # currencies = [
    #     #     Currencies(name=key, value=value)
    #     #     for key, value in dict(json.load(file)).items()
    #     # ]
    #     # Currencies.objects.bulk_create(currencies)
    currency = Currencies.objects.find()
    print(currency.count())
    if currency.count() > 0:
        print(currency[0].value)
