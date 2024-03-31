from django.shortcuts import render, redirect

from .models import Usuario
from .forms import CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def userLogin(request):
    context = {}
    return render(request, 'usuarios/login.html', context)


def userRegister(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada para ' + user)
            return redirect('user-login')
            
    context = {'form':form}
    return render(request, 'usuarios/register.html', context)


def addUsuario(request):
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

    return redirect('listagem-usuarios')