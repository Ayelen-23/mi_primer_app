import datetime
from django import forms


ANIO_ACTUAL = datetime.date.today().year


class PaisForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    continente = forms.CharField(max_length= 30)
    capital = forms.CharField(max_length= 50)

class OrganismosForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateField(
        widget= forms.SelectDateWidget(years=range(1940, ANIO_ACTUAL + 1)))
    activo = forms.BooleanField(required=False, initial=True)

class AcuerdosForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    descripcion = forms.CharField(widget=forms.Textarea, required=False)
    fecha_inicio = forms.DateField(
        widget= forms.DateInput(attrs={'type': 'date'}))
    activo = forms.BooleanField(required=False, initial=True)



