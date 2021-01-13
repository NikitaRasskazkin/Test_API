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
        currency = Currencies.objects.all()
        print(currency.count())
        if currency.count() > 0:
            resp = {
                'value': currency[0].value,
                'currency': name,
                'base': 'RUB'
            }
            return resp
        else:
            return make_response(ApiErrors.incorrect_parameter(), 404)

    @staticmethod
    def post():
        data = request.get_json()
        try:
            from_value = Currencies.objects.raw({'_id', data['from']})[0].value
            to_value = Currencies.objects.raw({'_id', data['to']})[0].value
        except TypeError:
            return make_response(ApiErrors.incorrect_parameter(), 404)
        resp = data
        resp['value'] = to_value / from_value * data['value']
        return resp


api.add_resource(CurrenciesRequest, '/get_currencies', '/get_currencies/<string:name>')


if __name__ == '__main__':
    app.run()
