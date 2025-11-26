from django.contrib import admin
from django.utils.html import format_html
from .models import Planta, UsoMedicinal, Regiao

class PlantaAdmin(admin.ModelAdmin):
    list_display = ('nome_cientifico', 'nome_popular', 'imagem_preview')
    readonly_fields = ('imagem_preview',)

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 150px; height: auto;" />', obj.imagem.url)
        return "(Sem imagem)"

    imagem_preview.short_description = 'Prévia da Imagem'

admin.site.register(Planta, PlantaAdmin)
admin.site.register(UsoMedicinal)
admin.site.register(Regiao)

