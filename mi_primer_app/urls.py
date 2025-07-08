
from django.urls import path
from.views import inicio, crear_pais, crear_organismo_internacional, crear_acuerdo_internacional, buscar_organismos, organismos

urlpatterns = [
    path('', inicio , name='inicio'),
    path('crear_pais/', crear_pais, name= 'crear_pais'),
    path('organismo_internacional/', crear_organismo_internacional, name='organismo internacional'),
    path('acuerdos_internacionales/', crear_acuerdo_internacional, name='acuerdo internacional'),
    path('organismos/', organismos, name='organismos'),
    path('organismo/buscar/', buscar_organismos, name='buscar_organismos')
    
    ]
    