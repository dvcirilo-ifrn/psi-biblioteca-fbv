from django.urls import path
from . import views

# namespace para urls
# evita conflito de nomes
# permite usar urls do tipo 'app_name:name'
# Ex. 'biblioteca:index'
app_name="biblioteca"
urlpatterns = [
    path("", views.index, name="index"),
    path("livros/", views.livros, name="livros"),
    path("livro/<int:id_livro>/", views.detalhar_livro, name="detalhar_livro"),
    path("pesquisa/", views.pesquisa, name="pesquisa"),
    path("meus-livros/", views.meus_livros, name="meus-livros"),
    path("favoritar/<int:id_livro>/", views.favoritar, name="favoritar"),
]
