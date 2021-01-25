from db.models import CurrencyModel


def get_currency_value(name: str):
    return CurrencyModel.objects.value(name)
