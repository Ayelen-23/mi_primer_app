
from django.urls import path
from.views import saludo, saludo_con_templates

urlpatterns = [
    path('Hola-mundo/', saludo),
    path('Hola-mundo-templates/', saludo_con_templates),
    
]