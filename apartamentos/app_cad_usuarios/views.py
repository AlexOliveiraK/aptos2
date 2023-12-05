from django.shortcuts import render, redirect
from .models import Usuario

def add_usuario(request):
    return render(request, 'usuarios/add_usuarios.html')

def usuarios(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)

def salvarUsuario(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    return redirect('listagem_usuarios')