from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Apartamentos

def catalogo(request):
    aptos = {
        'aptos': Apartamentos.objects.all()
    }

    return render(request, 'catalogo.html', aptos)

def novoApto(request):
    return render(request, 'novo_apto.html')

def salvarApto(request):
    novo_apto = Apartamentos()
    novo_apto.numero_apto= request.POST.get('numero_apto')
    novo_apto.morador = request.POST.get('morador')
    novo_apto.save()

    return redirect('catalogo-aptos')

def editaApto(request):
    if request.method == "POST":
        print("VEIO PELO POST >>>>>>>>>>>>>>>>>>")
        id_apto = request.POST.get('numero_apto')
        print(request)

        # apto = Apartamentos.objects.filter(id_apto = id_apto)
        # apto.numero_apto= request.POST.get('numero_apto')
        # apto.morador = request.POST.get('morador')
        
        # print(apto)

    elif request.method == "GET":
        print("VEIO PELO GET >>>>>>>>>>>>>>>>>>")
        # id_apto = request.GET.get('apto-numero')
        # print(id_apto)
        # apto = Apartamentos.objects.filter(id_apto = id_apto)
        # print(apto)

        # return render(request, 'edita_apto.html', apto)

    return redirect('catalogo-aptos')    
