from tkinter import CASCADE
from django.db import models

class PaineldeSenhasStatusSenha(models.Model):
    StatusSenha = models.CharField(max_lengt=255, null=False)
    tipo = models.CharField(max_length=255, null=False)
    categoria = models.CharField(max_length=255, null=False)
    senha = models.CharField(max_length=15, null=False)
    

    PaineldeSenhasStatusSenha = models.ManyToManyField('self')

        def senha(self, id_status_senha):
            PaineldeSenhasStatusSenha(solicicante=self, senha=id_status_senha).save()

