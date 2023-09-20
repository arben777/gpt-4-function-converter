import inspect


class FunctionConverter:
    def __init__(self, function):
        self.function = function

    def get_function_info(self):
        function_info = {
            'name': self.function.__name__,
            'description': inspect.getdoc(self.function),
            'parameters': {
                'type': 'object',
                'properties': {},
                'required': []
            }
        }

        params = inspect.signature(self.function).parameters
        for name, param in params.items():
            function_info['parameters']['properties'][name] = {'type': 'string'}
            if param.default == inspect.Parameter.empty:
                function_info['parameters']['required'].append(name)

        return function_info