from django.contrib import admin
from .models import CustoFixo, Despesa, Investimento

@admin.register(CustoFixo)
class CustoFixoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'usuario')
    search_fields = ('descricao', 'usuario__username')

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'usuario')
    search_fields = ('descricao', 'usuario__username')

@admin.register(Investimento)
class InvestimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')
    search_fields = ('nome',)
