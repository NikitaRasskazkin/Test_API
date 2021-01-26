from flask import make_response, request
from flask_restful import Resource

from errors import ApiErrors
from db import repository


class Currencies(Resource):
    @staticmethod
    def get(name=None):
        if not name:
            return make_response(ApiErrors.have_not_parameter('Currencies, the rate of which you need to get'), 404)
        value = repository.get_currency_value(name)
        if value:
            resp = {
                'value': value,
                'currency': name,
                'base': 'RUB'
            }
            return resp
        else:
            return make_response(ApiErrors.incorrect_parameter(), 404)

    @staticmethod
    def post(name=None):
        if name:
            return make_response(ApiErrors.incorrect_parameter(), 404)
        data = request.get_json()
        converted_currency = repository.get_converted_currency(data['from'], data['to'], data['value'])
        if converted_currency is not None:
            return {
                'from': data['from'],
                'to': data['to'],
                'value': converted_currency
            }
        else:
            return make_response(ApiErrors.incorrect_parameter(), 404)

    @staticmethod
    def put(name=None):
        if name:
            return make_response(ApiErrors.incorrect_parameter(), 404)
        data = request.get_json()
        base_value = repository.get_currency_value(data['base'])
        if repository.update_currency(data['currency'], base_value / data['value']) is not None:
            return make_response({'status': 'OK'}, 200)
        else:
            return make_response(ApiErrors.incorrect_parameter(), 404)  # TODO: refactor errors raise
