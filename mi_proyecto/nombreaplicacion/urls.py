from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('ejemplo/', views.vista_ejemplo, name='hola_mundo'),

]
