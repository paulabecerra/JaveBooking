from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError


class LoginView(TemplateView):
    def post(self, request):
        username = request.POST['username']
        password = requuest.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('usuarios:login')
        else:
            raise ValidationError(_('Username or password not valid'))
