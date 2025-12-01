from django.contrib import admin
from django.utils.html import format_html
from .models import Planta, UsoMedicinal, Regiao, FonteCientifica


# Inline para inserir usos medicinais diretamente dentro da planta
class UsoMedicinalInline(admin.TabularInline):
    model = UsoMedicinal
    extra = 1


class PlantaAdmin(admin.ModelAdmin):

    inlines = [UsoMedicinalInline]

    list_display = (
        'nome_popular',
        'nome_cientifico',
        'risco_extincao',
        'data_registro',
        'imagem_preview',
    )

    list_filter = (
        'risco_extincao',
        'regioes__tipo_bioma',
        'regioes',
    )

    search_fields = (
        'nome_popular',
        'nome_cientifico',
        'descricao',
        'regioes__nome',
        'regioes__tipo_bioma',
    )

    readonly_fields = ('imagem_preview',)

    filter_horizontal = ('regioes',)

    fieldsets = (
        ("Identificação da Planta", {
            'fields': ('nome_popular', 'nome_cientifico', 'descricao')
        }),
        ("Classificação", {
            'fields': ('risco_extincao', 'regioes')
        }),
        ("Imagem", {
            'fields': ('imagem', 'imagem_preview')
        }),
        ("Datas", {
            'fields': ('data_registro',),
        }),
    )

    def imagem_preview(self, obj):
        if obj.imagem:
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.imagem.url)
        return "(Sem imagem)"

    imagem_preview.short_description = "Prévia da Imagem"


admin.site.register(Planta, PlantaAdmin)

class UsoMedicinalAdmin(admin.ModelAdmin):
    list_display = ('planta', 'parte_utilizada', 'indicacao')
    list_filter = ('parte_utilizada',)
    search_fields = ('indicacao', 'modo_preparo')

class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_bioma')
    search_fields = ('nome', 'tipo_bioma')
    list_filter = ('tipo_bioma',)

class FonteCientificaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'fonte', 'planta')
    search_fields = ('titulo', 'autores', 'fonte')
    list_filter = ('ano', 'fonte')

admin.site.register(UsoMedicinal, UsoMedicinalAdmin)
admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(FonteCientifica, FonteCientificaAdmin)
