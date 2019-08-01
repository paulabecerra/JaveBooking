#Django
from django.urls import path

#Views
from usuarios import views

urlpatterns= [
    #Users
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login',
    ),
    path(
        route='logout/',
        view=views.LoginView.as_view(),
        name='logout',
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    )
]
