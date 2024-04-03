from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app_catalogo.models import Apartamentos
from app_catalogo.forms import ApartamentosForm

def catalogo(request):
    aptos = {
        'aptos': Apartamentos.objects.all()
    }

    return render(request, 'catalogo.html', aptos)

def novoApto(request):
    return render(request, 'novo_apto.html')

def salvaNovoApto(request):
    novo_apto = Apartamentos()
    novo_apto.numero_apto= request.POST.get('numero_apto')
    novo_apto.morador = request.POST.get('morador')
    novo_apto.aluguel = request.POST.get('aluguel')
    novo_apto.save()

    return redirect('catalogo-aptos')

def updateApto(request):
    novo_apto = Apartamentos.objects.filter(id_apto= request.POST.get('id_apto'))
    novo_apto.numero_apto= request.POST.get('numero_apto')
    novo_apto.morador = request.POST.get('morador')
    novo_apto.aluguel = request.POST.get('aluguel')
    novo_apto.save()

    return redirect('catalogo-aptos')

def editaApto2(request):
    if request.method == "POST":
        print("VEIO PELO POST >>>>>>>>>>>>>>>>>>")
        id_apto = request.POST.get('id_apto')
        print(id_apto)

        apto = Apartamentos.objects.filter(id_apto = id_apto)
        # apto.numero_apto= request.POST.get('numero_apto')
        # apto.morador = request.POST.get('morador')
        print(apto[0].id_apto)

    elif request.method == "GET":
        print("VEIO PELO GET >>>>>>>>>>>>>>>>>>")
        id_apto = request.GET.get('id_apto')
        print(id_apto)
        # id_apto = request.GET.get('apto-numero')
        # print(id_apto)
        # apto = Apartamentos.objects.filter(id_apto = id_apto)
        # print(apto)

        # return render(request, 'edita_apto.html', apto)

    return redirect('catalogo-aptos')

def editaApto(request):

    if request.method == 'GET':
        id_apto = request.GET.get(id_apto)
        apto = Apartamentos.objects.filter(id_apto = id_apto).first()
        form = ApartamentosForm(instance=apto)

        context = {
            'apto': apto,
            'form': form
        }

        return render(requast, 'edita_apto.html', context)

    elif request.method == 'POST':
        id_apto = request.POST.get('id_apto')
        apto = Apartamentos.objects.filter(id_apto = id_apto)

        if apto.count() == 1:
            context = {
                "aptos": apto.first()
            }

            return render(request, 'edita_apto.html', context)
