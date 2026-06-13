from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from accounts.models import  Perfil
from products.services.product_service import ProductService
from orders.models import  Pedido
from orders.services.order_service import OrderService
from orders.services.decorators import (
    Lanche,
    ExtraQueijo,
    Bacon,
    Catupiry,
)

from orders.services.delivery_strategy import (
    EntregaNormal,
    EntregaExpressa,
)

from orders.services.order_facade import OrderFacade
from products.gateways.product_gateway import ProductGateway




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
    
    def _montar_lanche(self, request, produto):

        lanche = Lanche(
            produto["nome"],
            produto["preco"]
        )

        adicionais = []

        if 'queijo' in request.POST:
            lanche = ExtraQueijo(lanche)
            adicionais.append('Queijo')

        if 'bacon' in request.POST:
            lanche = Bacon(lanche)
            adicionais.append('Bacon')

        if 'catupiry' in request.POST:
            lanche = Catupiry(lanche)
            adicionais.append('Catupiry')

        return lanche, adicionais

    def _validar_pagamento(self, perfil, pagamento):

        if pagamento == "cartao" and not perfil.cartao_cadastrado:
            raise ValueError("Você precisa cadastrar um cartão antes de pagar com cartão.")
        
    def _obter_strategy(self, tipo_entrega):

        return (
            EntregaExpressa()
            if tipo_entrega == "expressa"
            else EntregaNormal()
        )
            
    def _atualizar_endereco(self, perfil, request):

        perfil.endereco = request.POST['endereco']
        perfil.save()

    def post(self, request):

        produtos = ProductService.listar()

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

        pedido, resultado = OrderService.criar_pedido(
            perfil=perfil,
            produto=produto,
            request=request,
        )

        return render(
            request,
            'sucesso.html',
            {
                'pedido': pedido,
                'resultado': resultado
            }
        )

class HistoricoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        pedidos = Pedido.objects.filter(
            usuario=request.user
        ).order_by('-criado_em')

        return render(request, 'historico.html', {
            'pedidos': pedidos
        })