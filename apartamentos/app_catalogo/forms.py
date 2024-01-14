from django import forms
from app_catalogo.models import Apartamentos

class ApartamentosForm(forms.ModelForm):
    class Meta:
        model = Apartamentos
        #fields = ' __all__'
        fields = ('numero_apto', 'morador')
        #exclude = ('numero_apto', 'morador')
