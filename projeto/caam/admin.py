from django.contrib import admin
from .models import Especie, Raca, Animal
from django.utils.safestring import mark_safe

class EspecieAdmin(admin.ModelAdmin):
    pass

admin.site.register(Especie, EspecieAdmin)


class RacaAdmin(admin.ModelAdmin):
    list_display = 'nome', 'especie'

admin.site.register(Raca, RacaAdmin)


class AnimalAdmin(admin.ModelAdmin):
    search_fields = 'nome',
    list_filter = 'especie', 'raca'
    list_display = 'get_imagem', 'nome', 'especie', 'raca', 'data_nascimento', 'data_cadastro', 'data_adocao', 'tutor'

    def get_imagem(self, obj):
        return mark_safe(f"<img height='75' src='{obj.imagem.url}'/>")
    
    get_imagem.short_description = 'Imagem'


admin.site.register(Animal, AnimalAdmin)
