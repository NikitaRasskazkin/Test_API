from pymodm.queryset import QuerySet
from pymodm.manager import Manager


class CurrenciesQuerySet(QuerySet):
    def value(self, name):
        currency = self.raw({'name': name})
        if currency.count() > 0:
            return currency[0].value
        else:
            return None





if __name__ == '__main__':
    pass
