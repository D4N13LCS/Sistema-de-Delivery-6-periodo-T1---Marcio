from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.gateways.account_gateway import AccountGateway
from products.services.product_service import ProductService
from orders.gateways.order_gateway import OrderGateway
from orders.services.order_service import OrderService


# Create your views here.
class CriarPedidoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        produtos = ProductService.listar()

        perfil = AccountGateway.obter(request.user.id)

        if perfil is None:
            messages.error(
                request,
                "O serviço de contas está temporariamente indisponível."
            )
            return redirect("/")

        return render(request, 'pedido.html', {
            'produtos': produtos,
            'perfil': perfil
        })

    def _obter_perfil(self, request):

        return AccountGateway.obter(
            request.user.id
        )

    def post(self, request):

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

            AccountGateway.atualizar(
                usuario_id=request.user.id,
                endereco=request.POST["endereco"],
            )

            pedido, resultado = OrderService.criar_pedido(
                usuario_id=request.user.id,
                username=request.user.username,
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

    login_url = "/login/"

    def get(self, request):

        pedidos = OrderGateway.listar()

        if pedidos is None:
            messages.error(
                request,
                "O serviço de pedidos está temporariamente indisponível."
            )

            pedidos = []

        return render(
            request,
            "historico.html",
            {
                "pedidos": pedidos,
            }
        )