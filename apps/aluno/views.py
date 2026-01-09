from django.shortcuts import render, redirect
from apps.aluno.forms import AlunoForms
from apps.aluno.models import Aluno

def index(request):
    return render(request, 'index.html')

def lista(request):
    alunos = Aluno.objects.all()
    return render(request, "aluno/lista.html", {"alunos": alunos})

def cadastro(request):
    form = AlunoForms()

    if request.method == 'POST':
        form = AlunoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aluno/lista")
    
    return render(request, "aluno/cadastro.html", {"form": form})