from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Especie(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)  

    class Meta:
        verbose_name = "Espécie"
        verbose_name_plural = "Espécies"

    def __str__(self):
        return self.nome


class Raca(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)  
    especie = models.ForeignKey(Especie, verbose_name='Espécie', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Raça"
        verbose_name_plural = "Raças"

    def __str__(self):
        return f'{self.nome} - {self.especie}'


class Animal(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=100)  
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", null=True, blank=True)
    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=1,  
        choices=[["M", 'Masculino'], ['F', 'Feminino']]
    )
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(verbose_name='Imagem', upload_to='animais')
    especie = models.ForeignKey(Especie, verbose_name='Espécie', on_delete=models.CASCADE)
    raca = models.ForeignKey(Raca, verbose_name='Raça', on_delete=models.CASCADE)

    data_cadastro = models.DateField(verbose_name="Data de Cadastro", auto_created=True, default=timezone.now)
    data_adocao = models.DateField(verbose_name="Data de Adoção", null=True, blank=True)
    tutor = models.ForeignKey(User, verbose_name='Tutor', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"

    def __str__(self):
        return self.nome
