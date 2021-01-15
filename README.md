# Currencies REST API

API для получения курсов валют.

## Available methods

### Получение курсов валют

[GET] ```/api/currencies/<string:currencies_name>```

Получение курса валюты относительно Рубля.

##### Параметры
 - currencies_name - название валюты. Например ```USD```

##### Ответ

```
{
  "value": <double:currency_rate>,
  "currency": "USD",
  "base": "RUB"
}
```

[POST] ```/api/currencies```

##### Заголовок запроса

```Content-Type: application/json```

##### Тело

```
{
    "from": <string:currency>,
    "to": <string:currency>,
    "value": <int:value>
}
```

- from - валюта которую нужно конвертировать
- to - валюта в которую нужно конвертировать ```from```
- value - количество валюты ```from```

##### Ответ

```
{
    "from": <string:currency>,
    "to": <string:currency>,
    "value": <int:value>
}
```

- from - валюта, которая была конвертирована
- to - валюта в которую была конвертирована ```from```
- value - переведённое значение ```from``` в ```to```

## List of currencies

- CAD
- HKD
- ISK
- PHP
- DKK
- HUF
- CZK
- GBP
- RON
- SEK
- IDR
- INR
- BRL
- RUB
- HRK
- JPY
- THB
- CHF
- EUR
- MYR
- BGN
- TRY
- CNY
- NOK
- NZD
- ZAR
- USD
- MXN
- SGD
- AUD
- ILS
- KRW
- PLN

## Project deployment

##### Список зависимостей

- Flask==1.1.2
- Flask-RESTful==0.3.8
- pymodm==0.4.3
- pymongo==3.11.0
- pytest==6.0.1

Для установки всех зависимостей в консоль необходимо установить python 3.9 и ввести следующие команды:
```
python -m pip install flask==1.1.2
python -m pip install flask-restful==0.3.8
python -m pip install pymodm==0.4.3
python -m pip install pymongo==3.11.2
python -m pip install pytest==6.2.1
```