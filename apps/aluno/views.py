from django.shortcuts import render, redirect
from apps.aluno.forms import AlunoForms

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    form = AlunoForms()

    if request.method == 'POST':
        form = AlunoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("aluno/lista")
    
    return render(request, "aluno/cadastro.html", {"form": form})