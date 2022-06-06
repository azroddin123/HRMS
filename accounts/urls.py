from multiprocessing.spawn import import_main_path
from django.contrib import admin
from django.urls import path
from .views import * 

urlpatterns = [
    path('register',RegisterApi.as_view()),
    path('login',LoginApi.as_view()),
    path('user',UserApi.as_view())
]