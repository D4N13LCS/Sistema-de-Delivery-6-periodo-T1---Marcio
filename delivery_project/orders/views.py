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

# Create your views here.
class CriarPedidoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        produtos = Produto.objects.all()

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

    def post(self, request):

        produtos = Produto.objects.all()

        perfil, created = Perfil.objects.get_or_create(
            usuario=request.user,
            defaults={
                'saldo': 200
            }
        )

        produto = Produto.objects.get(
            id=request.POST['produto']
        )

        lanche = Lanche(
            produto.nome,
            produto.preco
        )

        adicionais = []

        if 'queijo' in request.POST:

            lanche = ExtraQueijo(lanche)

            adicionais.append("Queijo")

        if 'bacon' in request.POST:

            lanche = Bacon(lanche)

            adicionais.append("Bacon")

        if 'catupiry' in request.POST:

            lanche = Catupiry(lanche)

            adicionais.append("Catupiry")

        tipo_entrega = request.POST['entrega']

        pagamento = request.POST['pagamento']

        if pagamento == 'cartao' and not perfil.cartao_cadastrado:

            messages.warning(
                request,
                'Você precisa cadastrar um cartão antes de pagar com cartão.'
            )

            return redirect('/conta/')

        strategy = (
            EntregaExpressa()
            if tipo_entrega == 'expressa'
            else EntregaNormal()
        )


        subtotal = lanche.preco()

        taxa = strategy.calcular(subtotal)

        entrega = {
            "tipo": tipo_entrega,
            "taxa": taxa,
            "pagamento": pagamento
        }

        perfil.endereco = request.POST['endereco']

        perfil.save()

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

            return render(request, 'sucesso.html', {
                'pedido': pedido,
                'resultado': resultado
            })

        except Exception as erro:

            return render(request, 'pedido.html', {
                'produtos': produtos,
                'erro': str(erro),
                'perfil': perfil
            })


class HistoricoView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        pedidos = Pedido.objects.filter(
            usuario=request.user
        ).order_by('-criado_em')

        return render(request, 'historico.html', {
            'pedidos': pedidos
        })