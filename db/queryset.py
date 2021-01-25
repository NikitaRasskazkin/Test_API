from pymodm.queryset import QuerySet


class CurrenciesQuerySet(QuerySet):
    def value(self, name):
        currency = self.raw({'name': name})
        if currency.count() > 0:
            return currency[0].value
        else:
            return None


if __name__ == '__main__':
    pass
