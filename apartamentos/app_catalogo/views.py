from django.shortcuts import render
from .models import Apartamentos

# Create your views here.
def catalogo(request):
    novo_apto = Apartamentos()

    # novo_apto.numero_apto= request.POST.get('numero_apto')
    # novo_apto.morador = request.POST.get('morador')
    # novo_apto.save()

    aptos = {
        'aptos': Apartamentos.objects.all()
    }

    return render(request, 'catalogo.html', aptos)

def novoapto(request):
    return render(request, 'novoapto.html')
