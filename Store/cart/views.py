from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime


def cart_by_date(request, date_add):
    date_add_check = '2025-03-07'
    if date_add != datetime.strptime(date_add_check, '%Y-%m-%d'):
        return HttpResponseNotFound('<h1>Ошибка! В данный день вы не добавляли товара в карзину</h1')
    return HttpResponse('<h1>Тут добавленные товары в день добавления</h1>')

def cart(request):
    if request.GET:
        print(request.GET)
    return HttpResponse('<h1>Тут будет корзина товаров</h1>')