from django.db import models

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nome = models.TextField()
    cpf = models.IntegerField(unique=True)
    email = models.EmailField()
    saldo = models.FloatField()
    senha = models.TextField()
    #nascimento = models.DateField(null=True)
    


