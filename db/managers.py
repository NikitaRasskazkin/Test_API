from pymodm.manager import Manager
from db.queryset import CurrenciesQuerySet


manager = Manager.from_queryset(CurrenciesQuerySet)
