#Django
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

#utilities
from django.utils.decorators import method_decorator

#Forms
from usuarios.forms import SignupForm

#models
from usuarios.models import Profile


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
                template_name='users/login.html'
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
#-------ESTA VISTA A VECES SE ROMPE Y NO ENTIENDO POR QUÉ------------#
class LogoutView(TemplateView):
    def get(self, request):
        logout(request)
        return redirect('usuarios:login')


#Users sign up view
class SignupView(TemplateView):
#--------THIS WHOLE PROCESS WORKS FINE-----------------------#
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email')
            )
            user.save()
            profile = Profile.objects.create(
                user=user
            )
            login(request, user)
            return redirect('newsfeed:home')
        else:
            #form = SignupForm()
            return render(
                request=request,
                template_name='users/signup.html'
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
