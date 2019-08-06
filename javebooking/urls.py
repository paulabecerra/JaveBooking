#JaveBooking Urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
    path('newsfeed/', include(('newsfeed.urls', 'newsfeed'), namespace='newsfeed')),
    path('book/', include(('reservas.urls', 'reservas'), namespace='reservas'))
]
