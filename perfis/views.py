# experiencein/perfis/views.py 

# código anterior omitido
from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil, Convite

# importando redirect
from django.shortcuts import redirect

def index(request):
    return render(request, 'index.html', {'perfis' : Perfil.objects.all(), 'perfil_logado' : get_perfil_logado(request)})

# código posterior omitido

def exibir(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    ja_e_contato = perfil in perfil_logado.contatos.all()
    return render(request, 'perfil.html', {'perfil' : perfil, 'perfil_logado' : get_perfil_logado(request), 'ja_e_contato' : ja_e_contato})

   # perfil = Perfil()

   # if perfil_id == 1:
       # perfil = Perfil('Fábio Henrique', 'fabio.oliveira@ifb.edu.br', '222222', 'IFB')
    # if perfil_id == 2:
       # perfil = Perfil('Elon Musk', 'elon.musk@tesla.com', '333333', 'Tesla')
    
    # perfil = perfil = Perfil.objects.get(id=perfil_id) 

     

def get_perfil_logado(request):
    return Perfil.objects.get(id=1)

def convidar(request, perfil_id):
    
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar (perfil_a_convidar)
    
    # realizando redirecionamento
    return redirect('index')

def aceitar(request, convite_id):
  convite = Convite.objects.get(id=convite_id)
  convite.aceitar()
  return redirect('index')

def get_perfil_logado(request):
    return Perfil.objects.get(id=1) 

