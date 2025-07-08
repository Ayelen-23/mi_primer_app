
from django.urls import path
from.views import inicio, crear_pais, crear_organismo_internacional

urlpatterns = [
    path('', inicio , name='inicio'),
    path('crear_pais/', crear_pais, name= 'crear_pais'),
    path('organismo_internacional/', crear_organismo_internacional, name='organismo internacional')
    
    
    ]
    