from pymodm import MongoModel, fields
from pymodm.connection import connect
from pymongo.write_concern import WriteConcern
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
currencies = client.projectDB.currencies

# connect('mongodb://localhost:27017/projectDB2', alias='main-app')
#
#
# class Currencies(MongoModel):
#     name = fields.CharField(primary_key=True)
#     value = fields.FloatField()
#
#     class Meta:
#         write_concern = WriteConcern(j=True)
#         connection_alias = 'main-app'
#
#     Currencies(name='USD', value=15).save()
