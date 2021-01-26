from flask import request
from flask_restful import Resource

from validation.validation import validate_currency_post, validate_currency_put
from responses.responses import make_currency_response
from db import repository
from exeptions import exeptions


class Currencies(Resource):
    @staticmethod
    def get(name=None):
        if not name:
            raise exeptions.InvalidParameter
        value = repository.get_currency_value(name)
        if value:
            return make_currency_response('GET', name=name, value=value)
        else:
            raise exeptions.InvalidParameter

    @staticmethod
    def post(name=None):
        if name:
            raise exeptions.InvalidParameter
        data = validate_currency_post(request.get_json())
        converted_currency = repository.get_converted_currency(data['from'], data['to'], data['value'])
        if converted_currency is not None:
            return make_currency_response('POST', from_cur=data['from'], to_cur=data['to'], value=converted_currency)
        else:
            raise exeptions.InvalidHeader

    @staticmethod
    def put(name=None):
        if name:
            raise exeptions.InvalidParameter
        data = validate_currency_put(request.get_json())
        base_value = repository.get_currency_value(data['base'])
        if repository.update_currency(data['currency'], base_value / data['value']) is not None:
            return make_currency_response('PUT')
        else:
            raise exeptions.InvalidHeader
