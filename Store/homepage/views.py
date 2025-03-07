from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def homepage(request):
    return HttpResponse(f'''<h1>
                        Store
                        </h1>
                        <ul style="font-size: 20px">
                        <li style="display: inline-block"><a href="catalog/1">Первый товар</a></li>
                        <li style="display: inline-block"><a href="catalog/2">Второй товар</a></li>
                        <li style="display: inline-block"><a href="catalog/3">Третий товар</a></li>
                        <li style="display: inline-block"><a href="catalog/4">Четвертый товар</a></li>
                        </ul>
                        <p><a href="cart">Корзина</a></p>''')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

