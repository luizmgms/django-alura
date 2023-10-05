from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria", "legenda", "descricao")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome", "descricao")

admin.site.register(Fotografia, ListandoFotografias)
