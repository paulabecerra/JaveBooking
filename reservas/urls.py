#Django
from django.urls import path

#Views
from reservas import views

urlpatterns = [
    path(
        route='book/',
        view=views.TeacherSchedule.as_view(),
        name='book'
    )
]
