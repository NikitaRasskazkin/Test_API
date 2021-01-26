from db.models import models
import json
import os


def insert_all_models_data():
    for model in models:
        insert_model_data(model)


def insert_model_data(model):   # TODO: refactor open line
    with open(f'{os.path.abspath(__file__)[:-15]}/data/{model.__name__.lower()}.json', encoding='utf-8') as file:
        currencies = [
            model(name=key, value=value)
            for key, value in dict(json.load(file)).items()
        ]
        model.objects.bulk_create(currencies)
