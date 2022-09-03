import inspect

backend_url = 'http://127.0.0.1:8080'


def print_r(response):
    print(inspect.stack()[1][3], ': ', response)
