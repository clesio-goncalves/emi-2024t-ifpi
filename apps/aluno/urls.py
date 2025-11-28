from django.urls import path
from apps.aluno.views import cadastro

urlpatterns = [
    path("cadastro/", cadastro, name="cadastro"),
]