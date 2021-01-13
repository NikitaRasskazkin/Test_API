from pymodm.queryset import QuerySet
from pymodm.manager import Manager


class CurrenciesQuerySet(QuerySet):
    def find(self):
        return self.raw({'_id': 'USD'})


manager = Manager.from_queryset(CurrenciesQuerySet)


if __name__ == '__main__':
    pass
