from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import CadastroForm

def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Usuário {username} criado com sucesso!")
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, "registration/cadastro.html", {"form": form})

def perfil(request):
    return render(request, "registration/perfil.html")
