from django.db import models


class Disciplina(models.Model):
    nome = models.CharField(verbose_name="Nome")

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.nome

class Trabalho(models.Model):
    nome = models.CharField(verbose_name="Nome")
    disciplina = models.ForeignKey(Disciplina, verbose_name= "Disciplina", on_delete=models.CASCADE)
    data_prevista_entrega = models.DateField(verbose_name="Data Prevista para Entrega")
    data_entrega = models.DateField(verbose_name="Data da Entrega", null=True, blank=True)
    
    class Meta:
        verbose_name = "Trabalho"
        verbose_name_plural = "Trabalhos"

    def __str__(self):
        return f"{self.nome} ({self.disciplina})"