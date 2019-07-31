#Django
from django.urls import path
from django.views.generic import TemplateView

#Views
from usuarios import views

urlpatterns= [
    #Users
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    )
]
