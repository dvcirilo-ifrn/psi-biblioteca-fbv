from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    avatar = models.ImageField(
        upload_to="usuarios/avatar/",
        blank=True
    )
    nascimento = models.DateField() 

    def __str__(self):
        return self.first_name
    
    @property # permite acessar o método como uma propriedade, sem ()
    def idade(self):
        hoje = timezone.localdate()
        # defeito: pra quem nasceu no dia 29/02, só atualiza no dia 01/03
        return hoje.year - self.nascimento.year - ((hoje.month, hoje.day) < (self.nascimento.month, self.nascimento.day))
