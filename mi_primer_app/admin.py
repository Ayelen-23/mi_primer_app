from django.contrib import admin

# Register your models here.
from .models import Pais

register_models = [Pais]

admin.site.register(register_models)