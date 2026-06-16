from accounts.gateways.account_gateway import AccountGateway
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

        resultado = AccountGateway.criar(user.id)

        if resultado is None:
            user.delete()  # evita usuário órfão

            messages.error(
                request,
                "Não foi possível criar seu perfil no momento. Tente novamente."
            )

            return redirect("/register/")

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

        perfil = AccountGateway.obter(request.user.id)

        if perfil is None:
            messages.error(
                request,
                "O serviço de contas está indisponível no momento."
            )
            return redirect("/")

        return render(request, 'conta.html', {
            'perfil': perfil
        })

    def post(self, request):

        resultado = AccountGateway.atualizar(
            usuario_id=request.user.id,
            endereco=request.POST["endereco"],
            numero_cartao=request.POST["numero_cartao"],
            nome_cartao=request.POST["nome_cartao"],
            validade_cartao=request.POST["validade_cartao"],
        )

        if resultado is None:
            messages.error(
                request,
                "Não foi possível atualizar suas informações. O serviço de contas está indisponível."
            )
            return redirect("/conta/")

        messages.success(
            request,
            "Informações atualizadas!"
        )

        return redirect("/conta/")