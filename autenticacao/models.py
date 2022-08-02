from django.db import models

class UserJob(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    senha = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
    
