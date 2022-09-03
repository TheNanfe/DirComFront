from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.get_customer, name='get_user'),
    path('', views.list_users, name='list_users'),
    path('create/', views.add_user, name='create_user')
]