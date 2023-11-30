from django.contrib import admin

# Register your models here.
from .models import Apartamentos

class ApartamentosAdmin(admin.ModelAdmin):
    """
    Classe para descrever o form de edicao,criacao e detail do model
    """
    save_on_top = True 
    list_display = ["morador","numero_apto"]
    search_fields =["morador","numero_apto"]
    list_editable = ["numero_apto"]


admin.site.register(Apartamentos,ApartamentosAdmin)