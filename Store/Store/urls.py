from django.urls import path, include
from homepage.views import page_not_found

handler404 = page_not_found

urlpatterns = [
    path("", include("homepage.urls")),
    path("catalog/", include("catalog.urls")),
    path("cart/", include("cart.urls")),
]
