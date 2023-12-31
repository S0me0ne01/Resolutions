from django.contrib import admin
from django.urls import path

from .views import *

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'main'

urlpatterns = [
    #Homepage
    path('', getResa, name = 'homepage'),
    path('random/', random_res, name = 'random_res'),
    path('formats/', format_options, name = 'format_options'),
    path('categories/', category_options, name = 'category_options'),
    path('create/resolution/', create_resolution, name = 'create_resolution'),
    path('resolution/delete/<str:pk>/', delete_resolution, name = 'delete_resolution'),
]
