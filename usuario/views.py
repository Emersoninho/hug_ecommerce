from django.shortcuts import render, redirect
from.forms import RegistroForm
from.models import Usuario
from django.contrib.auth import authenticate, login

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])
            usuario.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request,'registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        usuario = authenticate(request, email=email, senha=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
    return render(request, 'login.html')