
from django import forms


class PaisForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    continente = forms.CharField(max_length= 30)
    capital = forms.CharField(max_length= 50)

class OrganismosForm(forms.Form):
    nombre = forms.CharField(max_length= 50)
    descripcion = forms.CharField(widget=forms.Textarea)
    paises_miembros = forms.ModelMultipleChoiceField(PaisForm.object.all)
    



