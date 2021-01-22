# Currencies REST API

API для получения курсов валют.

## Project deployment

### Docker

Для установки веб сервиса используется утилита ```docker-compose```. Для её использования необходимо установить:

- Docker: v20.10.2
- docker-compose: 1.27.4

Для сборки проекта введите следующую команду из корневой папки проекта:

```docker-compose build```

Для запуска контейнеров с вэб сервисом введите:

```docker-compose up -d```

### Virtualenv

Для установки вэб сервис без использования ```Docker``` 
вам необходимо самостоятельно установить ```MongoDB```. 
После чего создайте виртуальное окружение вашего проекта:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask setup
gunicorn -b :5000 app:app
```

#### Требования
- python: 3.9
- MongoDB: 4.4

#### Переменные среды

Для изменения стандартного подключения к ```mongo``` можно отредактировать файл 
```.env```

Используются следующие переменные среды:
- DB_CONNECT: строка подключения к `mongo`
- DB_NAME: иня базы данных

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
