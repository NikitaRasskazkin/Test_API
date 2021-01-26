def make_currency_response(method: str, **kwargs):
    if method == 'GET':
        return {
            'value': kwargs['value'],
            'currency': kwargs['name'],
            'base': 'RUB'
        }
    elif method == 'POST':
        return {
            'value': kwargs['value'],
            'from': kwargs['from_cur'],
            'to': kwargs['to_cur']
        }
    elif method == 'PUT':
        return {'status': 'OK'}
