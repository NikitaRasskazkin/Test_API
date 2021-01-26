from pymodm import MongoModel, fields


from db.managers import manager
from db.base import BaseModel


class Currency(MongoModel, BaseModel):
    name = fields.CharField()
    value = fields.FloatField()
    objects = manager()


models = [Currency]

if __name__ == '__main__':
    pass
