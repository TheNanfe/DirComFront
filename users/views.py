from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.urls import reverse


import apis.apis as backend
# Create your views here.


@require_http_methods(['GET', 'PUT', 'POST'])
def get_customer(request, pk):
    if request.method == 'GET':
        response = backend.get_user_by_id(pk)
        if response.status_code == 200:
            context = {'customer_details': response.json()}
            return render(request, 'customer_details.html', context)
    if request.method == 'POST':
        data = request.POST
        user_id = data.get('user_id')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')
        status = data.get('status')
        response = backend.edit_user(user_id, first_name, last_name, email, address, phone, status, pk)
        if response.status_code == 200:
            return reverse('list_users')

    return reverse('list_users')


@require_http_methods(['GET'])
def list_users(request):
    response = backend.get_user_list()
    if response.status_code == 200:
        user_list = response.json()
        context = {'user_list': user_list}
        return render(request, 'list_users.html', context=context)


@require_http_methods(['POST'])
def delete_user(request):
    return HttpResponse(status=400)


@require_http_methods(['GET', 'POST'])
def add_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')

    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')
        status = data.get('status')
        password = data.get('password')

        response = backend.add_user(username, first_name, last_name, email, address, phone, password, status)

    return reverse('user_list')

