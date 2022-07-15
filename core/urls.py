
from django.urls import path
from .views import *


urlpatterns = [
    path('', root ),
    path('home', home, name='home'),
    path('clima/', clima, name='clima'),
    path('productos/', productos, name='productos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('salir/', salir, name='salir'),
]
