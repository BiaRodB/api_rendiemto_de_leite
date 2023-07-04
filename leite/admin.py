from django.contrib import admin
from leite.models import *

# Register your models here.
class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'senha')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Pessoa, Pessoas)


class Vacas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'raca', 'idade', 'kg')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Vaca, Vacas)


class Rendimentos(admin.ModelAdmin):
    list_display = ('id', 'litros', 'dia')
    list_display_links = ('id', 'litros')
    search_fields = ('litros',)
    list_per_page = 20

admin.site.register(Rendimento, Rendimentos)

