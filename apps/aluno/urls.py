from django.urls import path
from apps.aluno.views import cadastro, lista

urlpatterns = [
    path("cadastro/", cadastro, name="aluno/cadastro"),
    path("lista/", lista, name="aluno/lista")
]