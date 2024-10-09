from django.contrib import admin
from .models import Usuario, PerfilUsuario, CustoFixo, TipoDespesa, DespesasExtras, Investimentos, Relatorio

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'login')
    search_fields = ('nome', 'login')

@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'patrimonio_liquido', 'salario')
