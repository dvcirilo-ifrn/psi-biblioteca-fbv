from django.urls import path
from . import views

# namespace para urls
# evita conflito de nomes
# permite usar urls do tipo 'app_name:name'
# Ex. 'dashboard:index'
app_name="dashboard"
urlpatterns = [
    path("", views.index, name="index"),
]
