from django.urls import path
from . import views

urlspattern = [
    path ('', views.PaineldeSenhas, name='PaineldeSenhas'),
    path ('perfis/<int:id_senha>', views.exibir, name='exibir'),
]