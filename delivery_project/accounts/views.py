from accounts.models import Perfil
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .services.password_validator import senha_valida

class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')

    def post(self, request):

        username = request.POST['username']

        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'Este usuário já existe.'
            )

            return redirect('/register/')

        if not senha_valida(password):

            messages.error(
                request,
                'Senha inválida. Verifique os requisitos.'
            )

            return redirect('/register/')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        Perfil.objects.create(
            usuario=user,
            saldo=200
        )

        messages.success(
            request,
            'Conta criada com sucesso!'
        )

        return redirect('/login/')



class LoginView(View):

    def get(self, request):

        return render(request, 'login.html')

    def post(self, request):

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            next_url = request.GET.get('next')

            if next_url:

                return redirect(next_url)

            return redirect('/')

        messages.error(
            request,
            'Usuário ou senha inválidos.'
        )

        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect('/login/')


class ContaView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        perfil, created = Perfil.objects.get_or_create(
            usuario=request.user,
            defaults={
                'saldo': 200
            }
        )

        return render(request, 'conta.html', {
            'perfil': perfil
        })

    def _atualizar_endereco(self, perfil, request):

        perfil.endereco = request.POST['endereco']

    def _atualizar_cartao(self, perfil, request):

        perfil.numero_cartao = request.POST[
            'numero_cartao'
        ]

        perfil.nome_cartao = request.POST[
            'nome_cartao'
        ]

        perfil.validade_cartao = request.POST[
            'validade_cartao'
        ]

    def _atualizar_status_cartao(self, perfil):

        perfil.cartao_cadastrado = bool(
            perfil.numero_cartao
        )

    def post(self, request):

        perfil = Perfil.objects.get(
            usuario=request.user
        )

        self._atualizar_endereco(
            perfil,
            request
        )

        self._atualizar_cartao(
            perfil,
            request
        )

        self._atualizar_status_cartao(
            perfil
        )

        perfil.save()

        messages.success(
            request,
            'Informações atualizadas!'
        )

        return redirect('/conta/')