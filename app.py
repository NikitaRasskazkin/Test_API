from flask import Flask
from flask_restful import Api

from api.currencies import Currencies


app = Flask(__name__)
api = Api(app)


api.add_resource(Currencies, '/api/currencies', '/api/currencies/<string:name>')


if __name__ == '__main__':
    app.run()
