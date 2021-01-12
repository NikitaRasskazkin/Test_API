from models import currencies
from flask import Flask, make_response, request
from flask_restful import Api, Resource
from errors import ApiErrors


app = Flask(__name__)
api = Api(app)


class Currencies(Resource):
    @staticmethod
    def get(name=None):
        if not name:
            return make_response(ApiErrors.have_not_parameter('Currencies, the rate of which you need to get'), 404)
        resp = currencies.find_one({'name': name})
        if resp:
            resp = {
                'value': resp['value'],
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
            from_value = currencies.find_one({'name': data['from']})['value']
            to_value = currencies.find_one({'name': data['to']})['value']
        except TypeError:
            return make_response(ApiErrors.incorrect_parameter(), 404)
        resp = data
        resp['value'] = to_value / from_value * data['value']
        return resp


api.add_resource(Currencies, '/get_currencies', '/get_currencies/<string:name>')


if __name__ == '__main__':
    app.run()
