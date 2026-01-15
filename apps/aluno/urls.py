from django.urls import path
from apps.aluno.views import cadastro, lista, edita

urlpatterns = [
    path("cadastro/", cadastro, name="aluno/cadastro"),
    path("lista/", lista, name="aluno/lista"),
    path("edita/<int:id>", edita, name="aluno/edita")
]