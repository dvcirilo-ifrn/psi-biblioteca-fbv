from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import Usuario

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.instance._meta.get_fields():
            print(field.name)
            # if field.name not in ['id', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions', 'date_joined']:
                # self.fields[field.name] = self.fields.get(field.name)

