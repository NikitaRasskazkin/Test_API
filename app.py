from models import currencies
from flask import Flask, make_response, request
from flask_json_schema import JsonValidationError, JsonSchema
from validation_schemas import post_schema


app = Flask(__name__)
schema = JsonSchema(app)


@app.errorhandler(JsonValidationError)
def validation_error(error_object):
    body = {'error': error_object.message, 'errors': [error.message for error in error_object.errors]}
    return make_response(body, 400)


@app.route('/<name>', methods=['GET'])
def get_currencies(name):
    resp = currencies.find_one({'name': name})
    if resp:
        resp = {
            'value': resp['value'],
            'currency': name,
            'base': 'RUB'
        }
        return make_response(resp, 200)
    else:
        return make_response(f'ERROR: currency \"{name}\" not found', 404)


@app.route('/currencies', methods=['POST'])
@schema.validate(post_schema)
def post_currencies():
    data = request.get_json()
    print(data)
    try:
        from_value = currencies.find_one({'name': data['from']})['value']
        to_value = currencies.find_one({'name': data['to']})['value']
    except TypeError:
        return make_response('ERROR: the currency is specified incorrectly', 404)
    resp = data
    resp['value'] = to_value / from_value * data['value']
    return make_response(resp, 200)


if __name__ == '__main__':
    app.run()
