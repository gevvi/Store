from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound

# Create your views here.
def catalog(request, pk):
    if pk > 3:
        raise Http404()
        #return HttpResponseNotFound('<h1>Ошибка 404</h1> <p>Возможно товар еще не добавлен</p>')
    return HttpResponse(f'<h1>Вывод товара {pk}</h1>')



