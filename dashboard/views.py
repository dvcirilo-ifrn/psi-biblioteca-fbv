from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.urls import reverse_lazy
from contas.models import Usuario
from biblioteca.models import Livro

@login_required
@permission_required("biblioteca.add_livro", raise_exception=True)
def index(request):

    context = {
        "num_livros": Livro.objects.count(),
        "num_usuarios": Usuario.objects.count(),
        "num_favoritos": Livro.favoritos.through.objects.count(),
    }

    return render(request, "dashboard/index.html", context)

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, "dashboard/livros.html", {"livros": livros})

def criar_livro(request):
    pass

def ler_livro(request):
    pass

def editar_livro(request):
    pass

def remover_livro(request):
    pass

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "dashboard/usuarios.html", {"usuarios": usuarios})

def criar_usuario(request):
    pass

def ler_usuario(request):
    pass

def editar_usuario(request):
    pass

def remover_usuario(request):
    pass

def desabilitar_usuario(request):
    pass

def listar_favoritos(request):
    pass
