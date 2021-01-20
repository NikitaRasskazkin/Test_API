

class ApiErrors:
    @staticmethod
    def have_not_parameter(parameter_description: str):
        return {
            'Error': f'To use this method, specify the parameter: {parameter_description}'
        }

    @staticmethod
    def incorrect_parameter():
        return {
            'Error': 'The specified parameter is invalid'
        }
