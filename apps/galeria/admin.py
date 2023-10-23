from django.contrib import admin
from apps.galeria.models import Fotografia, Categoria

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome" ,"categoria", "legenda", "descricao", "publicada")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome", "descricao")
    list_filter = ("categoria", "usuario")
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)

class ListarCategorias(admin.ModelAdmin):
    list_display = ("id", "chave", "valor")
    list_display_links = ("id", "chave", "valor")
    search_fields = ("chave", "valor")
    list_per_page = 10

admin.site.register(Categoria, ListarCategorias)
