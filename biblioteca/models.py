from django.db import models
from django.conf import settings

class Livro(models.Model):
    ROMANCE = "RO"
    BIOGRAFIA = "BI"
    TECNICO = "TE"
    FICCAO = "FI"
    OUTROS = "OU"
    GENEROS = {
        ROMANCE: "Romance",
        BIOGRAFIA: "Biografia",
        TECNICO: "Técnico",
        FICCAO: "Ficção",
        OUTROS: "Outros",
    }

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano = models.PositiveIntegerField()
    genero = models.CharField(max_length=2, choices=GENEROS)
    capa = models.ImageField(upload_to="biblioteca/capas/", blank=True)
    sinopse = models.TextField(blank=True)
    favoritos = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.titulo
