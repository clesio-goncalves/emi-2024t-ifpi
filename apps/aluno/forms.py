from django import forms
from apps.aluno.models import Aluno

class AlunoForms(forms.ModelForm):
    class Meta:
        model = Aluno
        exclude = ["",]
        labels = {
            "matricula" : "Matrícula",
            "status" : "Ativo"
        }

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", 
                                            "autofocus": "autofocus"}),
            
            "matricula": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.CheckboxInput(attrs={"class": "form-control form-check-input"})
        }