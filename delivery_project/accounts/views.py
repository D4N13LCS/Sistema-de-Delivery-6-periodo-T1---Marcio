from accounts.gateways.account_gateway import AccountGateway
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .services.password_validator import password_validate

class RegisterView(View):

    def get(self, request):

        return render(request, 'register.html')

    def post(self, request):

        username = request.POST['username']

        password = request.POST['password']

        if User.objects.filter(username=username).exists():

            messages.error(
                request,
                'User already registered'
            )

            return redirect('/register/')

        if not password_validate(password):

            messages.error(
                request,
                'Invalid Password. Check the password requirements.'
            )

            return redirect('/register/')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        response = AccountGateway.create_profile(user.id)

        if response is None:
            user.delete()  

            messages.error(
                request,
                "Can't create your profile at the moment. Try later."
            )

            return redirect("/register/")

        messages.success(
            request,
            'Profile successfully registered!'
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
            'Either Invalid User or Password.'
        )

        return render(request, 'login.html')


class LogoutView(View):

    def get(self, request):

        logout(request)

        return redirect('/login/')


class ContaView(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        profile = AccountGateway.get_profile(request.user.id)

        if profile is None:
            messages.error(
                request,
                "The account service is not available at the moment. Try later"
            )
            return redirect("/")

        return render(request, 'conta.html', {
            'profile': profile
        })

    def post(self, request):

        response = AccountGateway.update_profile(
            user_id=request.user.id,
            address=request.POST["address"],
            card_number=request.POST["card_number"],
            card_name=request.POST["card_name"],
            card_expiration=request.POST["card_expiration"],
        )

        if response is None:
            messages.error(
                request,
                "Your data could not be updated. Account service is off"
            )
            return redirect("/conta/")

        messages.success(
            request,
            "Data successfully updated!"
        )

        return redirect("/conta/")