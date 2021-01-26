from pymodm.queryset import QuerySet


class CurrenciesQuerySet(QuerySet):
    def get_currency(self, name):
        currency = self.raw({'name': name})
        if currency.count() > 0:
            return currency[0].value
        else:
            return None

    def update_currencies(self, name: str, value: float):
        return self.raw({'name': name}).update({'$set': {'value': value}})


if __name__ == '__main__':
    pass
