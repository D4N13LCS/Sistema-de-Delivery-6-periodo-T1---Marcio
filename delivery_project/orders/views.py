from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import  Perfil
from products.services.product_service import ProductService
from orders.gateways.order_gateway import OrderGateway
from orders.services.order_service import OrderService


# Create your views here.
class CriarPedidoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        produtos = ProductService.listar()

        perfil, created = Perfil.objects.get_or_create(
            usuario=request.user,
            defaults={
                'saldo': 200
            }
        )

        return render(request, 'pedido.html', {
            'produtos': produtos,
            'perfil': perfil
        })

    def _obter_perfil(self, request):

        perfil, _ = Perfil.objects.get_or_create(
            usuario=request.user,
            defaults={
                'saldo': 200
            }
        )

        return perfil

    def post(self, request):

        perfil = self._obter_perfil(request)

        produto = ProductService.buscar_por_id(
            request.POST["produto"]
        )

        if produto is None:
            messages.error(
                request,
                "Produto não encontrado."
            )
            return redirect("/")
        
        try:
            tipo_entrega = request.POST["entrega"]
            tipo_pagamento = request.POST["pagamento"]

            adicionais_selecionados = {
                nome
                for nome in ("queijo", "bacon", "catupiry")
                if nome in request.POST
            }

            perfil.endereco = request.POST["endereco"]
            perfil.save()

            pedido, resultado = OrderService.criar_pedido(
                perfil=perfil,
                produto=produto,
                tipo_entrega=tipo_entrega,
                tipo_pagamento=tipo_pagamento,
                adicionais_selecionados=adicionais_selecionados,
            )

            return render(
                request,
                'sucesso.html',
                {
                    'pedido': pedido,
                    'resultado': resultado
                }
            )

        except ValueError as erro:
            messages.error(request, str(erro))
            return redirect("/pedido/")

class HistoricoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        pedidos = OrderGateway.listar()

        return render(request, 'historico.html', 
                {
                    'pedidos': pedidos
                }
        )