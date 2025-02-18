from django.shortcuts import render

def index(request):
    livros = [
        {
            "titulo": "Livro teste",
            "autor": "Autor teste",
            "ano": 2025,
            "genero": "comédia",
            "favoritos": 23,
            "favoritado": True,

         }
    ]
    return render(request, "biblioteca/index.html", {"livros": livros})
