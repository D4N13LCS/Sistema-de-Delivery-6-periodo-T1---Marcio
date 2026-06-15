from django.urls import path

from .views import list_orders, create_order

urlpatterns = [
    path("orders/", list_orders),
    path("orders/create/", create_order),
]