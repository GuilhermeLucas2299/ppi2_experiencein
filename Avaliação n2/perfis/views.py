from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import models
from django.shortcuts import redirect

def PaineldeSenhasStatusSenha(request):
    return render(request, 'PaineldeSenha.html', 'StatusSenha.html', {'perfis': PaineldeSenhasStatusSenha.objects.all()})

def exibir(request, id_senha):
    senha = PaineldeSenhasStatusSenha.all(id=id_senha)
    return render(request, 'PaineldeSenha.html', 'StatusSenha.html', {'perfis': PaineldeSenhasStatusSenha.objects.all()})


def PaineldeSenhasStatusSenha():
    return redirect('StatusSenha')

categoria = ()

if categoria == 1:
    categoria = categoria('Matricula')
if categoria == 2:
    categoria = categoria('Rematŕicula')
if categoria == 3:
    categoria = categoria('Diploma')

categoria = categoria = PaineldeSenhasStatusSenha.objects.all()

tipo = ()

if tipo == 1:
    tipo = tipo('Não Preferencial')
if tipo == 2:
    tipo = tipo('Preferencial')

tipo = tipo = PaineldeSenhasStatusSenha.objects.all()

