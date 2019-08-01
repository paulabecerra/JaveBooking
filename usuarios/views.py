#Django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError

#utilities
from django.utils.decorators import method_decorator

from usuarios.forms import SignupForm


#Users Login view
class LoginView(TemplateView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('newsfeed:home')
        else:
            return render(
                request=request,
                template_name='newsfeed/home.html'
            )

    def get(self, request):
        if not request.user.is_anonymous:
            return redirect('newsfeed:home')
        else:
            return render(
                request=request,
                template_name='users/login.html'
            )

#Users Logout view
@method_decorator(login_required, name='dispatch')
class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('users:login')


#Users sign up view
class SignupView(TemplateView):
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                full_name=form.cleaned_data.get('fullname'),
                email=form.cleaned_data.get('email')
            )
            user.save()
            login(request, user)
            return redirect('newsfeed:home')
        else:
            form = SignupForm()
            return render(
                request=request,
                template_name='usuarios/signup.html'
            )
            return redirect('usuarios:signup')

    def get(self, request):
        form = SignupForm()
        if not request.user.is_anonymous:
            return render(
                request=request,
                template_name='newsfeed/home.html'
            )
        else:
            return render(
                request=request,
                template_name='users/signup.html'
            )
