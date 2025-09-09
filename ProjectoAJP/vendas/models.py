
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.utils import timezone
import datetime

class Carro(models.Model):
    marca= models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200)
    ano_fabrico = models.IntegerField()
    distancia_percorrida = models.IntegerField()
    preco=models.IntegerField()
    imagem = models.CharField(max_length=200)



    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_matricua(self):
        return self.matricula

    def get_ano_fabrico(self):
        return self.ano_fabrico

    def get_distancia_percorrida(self):
        return self.distancia_percorrida

    def get_preco(self):
        return self.preco

    def get_imagem(self):
        return self.imagem\

    def __str__(self):
        return (self.marca + ', ' + self.modelo + ', ' + self.matricula +', ' + str(self.ano_fabrico) + ', '
                + str(self.distancia_percorrida) +', ' + str(self.preco) +', ' + self.imagem)


class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    morada = models.CharField(max_length=200)
    telefone = models.IntegerField()

    def get_Nome(self):
        return self.nome

    def get_Apelido(self):
        return self.apelido

    def get_Email(self):
        return self.email

    def get_Morada(self):
        return self.morada

    def get_Telefone(self):
        return self.telefone

    def __str__(self):
        return "nome: %s, apelido: %s, email: %s, morada: %s, telefone: %d, username: %s" \
               %(self.nome, self.apelido, self.email,self.morada, self.telefone, self.username)

class Resposta(models.Model):
    texto=models.CharField(max_length=200)

    def __str__(self):
        return self.texto

class Questao(models.Model):
    resposta = models.OneToOneField(Resposta, on_delete=models.CASCADE)
    questao_texto = models.CharField(max_length=200)
    pub_data =models.DateTimeField('data de publicacao')

    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now()-datetime.timedelta(days=1)

    def __str__(self):
        return self.questao_texto



