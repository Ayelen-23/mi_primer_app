from django.contrib import admin

# Register your models here.
from .models import Pais, Organismos, Acuerdos

register_models = [Pais, Organismos, Acuerdos]

admin.site.register(register_models)