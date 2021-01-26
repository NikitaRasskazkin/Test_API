from jsonschema import validate
from jsonschema.exceptions import ValidationError

from validation.schemas import *
from exeptions import exeptions


def validate_currency_post(body):
    try:
        validate(body, CURRENCY_POST)
        return body
    except ValidationError:
        raise exeptions.InvalidBody


def validate_currency_put(body):
    try:
        validate(body, CURRENCY_PUT)
        return body
    except ValidationError:
        raise exeptions.InvalidBody
