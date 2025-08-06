from django.contrib import admin
from .models import Disciplina, Trabalho

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = 'nome',

admin.site.register(Disciplina, DisciplinaAdmin)

class TrabalhoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'disciplina', 'data_prevista_entrega', 'data_entrega'
    list_filter = 'disciplina',
    exclude = 'data_entrega',

admin.site.register(Trabalho, TrabalhoAdmin)
