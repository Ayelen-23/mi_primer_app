from django.shortcuts import render, redirect

# Create your views here.

from .forms import PaisForm, OrganismosForm, AcuerdosForm
from .models import Pais, Organismos, Acuerdos

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
                descripcion = form.cleaned_data['descripcion'],
                fecha_inicio =form.cleaned_data["fecha_inicio"],
                activo = form.cleaned_data['activo']

                )

            nuevo_organismo.save()
            return redirect('inicio')
    else:
        form = OrganismosForm()
    return render(request, 'mi_primer_app/crear_organismo.html',{"form":form})
    
    
def crear_acuerdo_internacional(request):
    if request.method == "POST":
        form = AcuerdosForm(request.POST)
        if form.is_valid():
            nuevo_acuerdo = Acuerdos(
                nombre = form.cleaned_data["nombre"],
                descripcion = form.cleaned_data['descripcion'],
                fecha_inicio =form.cleaned_data["fecha_inicio"],
                activo = form.cleaned_data['activo']

                )

            nuevo_acuerdo.save()
            return redirect('inicio')
    else:
        form = OrganismosForm()
    return render(request, 'mi_primer_app/crear_acuerdos.html',{"form":form})


def organismos(request):
    organismos = Organismos.objects.all()
    return render(request, "mi_primer_app/organismo.html",{'organismo': organismos})
    
    
def buscar_organismos(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre','')
        organismos = Organismos.objects.filter(nombre__icontains=nombre)
        return render(request,'mi_primer_app/organismo.html',{'organismos':organismos,'nombre': nombre})
    

        
