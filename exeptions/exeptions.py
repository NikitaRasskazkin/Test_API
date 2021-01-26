from werkzeug import exceptions


class InvalidBody(exceptions.UnprocessableEntity):
    description = 'Invalid request body'


class InvalidParameter(exceptions.NotFound):
    description = 'This method does not support the <name> parameter'


class InvalidHeader(exceptions.UnprocessableEntity):
    description = 'Currency entered incorrectly'


