from django.contrib import admin
from django.urls import path
# from register_app import views
from .views import *

urlpatterns = [
    # path("", views.register_app name="register_app")
    path('register/', register),
    path('welcome/',welcome),
    path('login/',login),
]