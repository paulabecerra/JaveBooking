#Django
from django.urls import path

#Views
from newsfeed import views

urlpatterns= [
    path(
        route='home/',
        view=views.NewsFeedView.as_view(),
        name='home'
    )
]
