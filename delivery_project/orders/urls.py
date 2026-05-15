from django.urls import path
from .views import *

urlpatterns = [

    path('pedido/', CriarPedidoView.as_view()),
    path('historico/', HistoricoView.as_view()),

]