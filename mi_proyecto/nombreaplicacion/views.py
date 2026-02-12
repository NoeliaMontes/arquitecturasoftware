from django.shortcuts import render
from django.http import HttpResponse

def vista_ejemplo(request):
    return HttpResponse('Hola Mundo')
    
