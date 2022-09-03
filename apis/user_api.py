import requests
from conections.conections_utils import backend_url, print_r


def get_user_list():
    response = requests.get(backend_url + '/users/')
    print('get_user_list', response.status_code)
    return response


def get_user_by_id(pk):
    response = requests.get(backend_url + '/users/' + pk)
    print_r(response)
    return response


def edit_user(user_id, first_name, last_name, email, address, phone, status, pk):

    if status == 'True':
        status = 'ACTIVE'
    else:
        status = 'DELETED'

    data = {
        'user_id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'phone_number': phone,
        'status': status
    }
    response = requests.post(backend_url + '/users/' + pk, data=data)
    print('edit_user', response)
    return response


def add_user(username, first_name, last_name, email, address, phone, password, status='ACTIVE'):
    data = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'address': address,
        'phone_number': phone,
        'status': status,
        'password': password
    }
    response = requests.post(backend_url + '/users/create/', data=data)
    print_r(response)
