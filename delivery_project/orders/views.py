from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from accounts.models import  Perfil
from orders.models import  Pedido
from products.models import Produto
from orders.services.decorators import *
from orders.services.delivery_strategy import *
from orders.services.order_facade import OrderFacade
from products.gateways.product_gateway import ProductGateway



# Create your views here.
class CriarPedidoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        produtos = ProductGateway.listar()

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
            produto.nome,
            produto.preco
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

        if pagamento == 'cartao' and not perfil.cartao_cadastrado:

            raise ValueError(
                'Você precisa cadastrar um cartão antes de pagar com cartão.'
            )
        
    def _obter_strategy(self, tipo_entrega):

        if tipo_entrega == 'expressa':
            return EntregaExpressa()

        return EntregaNormal()
    
    def _atualizar_endereco(self, perfil, request):

        perfil.endereco = request.POST['endereco']
        perfil.save()

    def post(self, request):

        produtos = ProductGateway.listar()

        perfil = self._obter_perfil(request)

        produto = Produto.objects.get(
            id=request.POST['produto']
        )

        lanche, adicionais = self._montar_lanche(
            request,
            produto
        )

        pagamento = request.POST['pagamento']

        try:

            self._validar_pagamento(
                perfil,
                pagamento
            )

        except ValueError as erro:

            messages.warning(
                request,
                str(erro)
            )

            return redirect('/conta/')

        subtotal = lanche.preco()

        strategy = self._obter_strategy(
            request.POST['entrega']
        )

        taxa = strategy.calcular(subtotal)

        entrega = {
            "tipo": request.POST['entrega'],
            "taxa": taxa,
            "pagamento": pagamento
        }

        self._atualizar_endereco(
            perfil,
            request
        )

        try:

            pedido, resultado = (
                OrderFacade.finalizar_pedido(
                    perfil,
                    produto,
                    ", ".join(adicionais),
                    entrega,
                    subtotal
                )
            )

            return render(
                request,
                'sucesso.html',
                {
                    'pedido': pedido,
                    'resultado': resultado
                }
            )

        except Exception as erro:

            return render(
                request,
                'pedido.html',
                {
                    'produtos': produtos,
                    'erro': str(erro),
                    'perfil': perfil
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