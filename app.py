from db.models import Currencies
from flask import Flask, make_response, request
from flask_restful import Api, Resource
from errors import ApiErrors


app = Flask(__name__)
api = Api(app)


class CurrenciesRequest(Resource):
    @staticmethod
    def get(name=None):
        if not name:
            return make_response(ApiErrors.have_not_parameter('Currencies, the rate of which you need to get'), 404)
        value = Currencies.objects.value(name)
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
        from_value = Currencies.objects.value(data['from'])
        to_value = Currencies.objects.value(data['to'])
        if not from_value or not to_value:
            return make_response(ApiErrors.incorrect_parameter(), 404)
        resp = data
        resp['value'] = to_value / from_value * data['value']
        return resp


api.add_resource(CurrenciesRequest, '/api/currencies', '/api/currencies/<string:name>')


if __name__ == '__main__':
    app.run()
