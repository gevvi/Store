from django.urls import path, register_converter

from . import views, converters
register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('', views.cart),
    path('<date:date_add>', views.cart_by_date),
]
