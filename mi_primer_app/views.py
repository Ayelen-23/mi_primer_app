from django.shortcuts import render, redirect

# Create your views here.

from .forms import PaisForm, OrganismosForm
from .models import Pais, Organismos

def inicio(request):
    return render(request,'mi_primer_app/inicio.html')



def crear_pais(request):
    if request.method == "POST":
        form = PaisForm(request.POST)
        if form.is_valid():
            nuevo_pais = Pais(
                nombre = form.cleaned_data["nombre"],
                continente = form.cleaned_data['continente'],
                capital = form.cleaned_data['capital'],
                )

            nuevo_pais.save()
            return redirect('inicio')
    else:
        form = PaisForm()
    return render(request, 'mi_primer_app/crear_pais.html',{"form":form})

def crear_organismo_internacional(request):
    if request.method == "POST":
        form = OrganismosForm(request.POST)
        if form.is_valid():
            nuevo_organismo = Organismos(
                nombre = form.cleaned_data["nombre"],
                siglas= form.cleaned_data['siglas'],
                descripcion = form.cleaned_data['descripcion'],
                paises_miembros = form.cleaned_data["paises_miembros"],

                )

            nuevo_organismo.save()
            return redirect('inicio')
    else:
        form = OrganismosForm()
    return render(request, 'mi_primer_app/crear_organismo.html',{"form":form})
    
    
    
