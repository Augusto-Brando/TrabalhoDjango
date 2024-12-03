from django.contrib import admin
from .models import Usuario, PerfilUsuario, CustoFixo, DespesasExtras, Investimentos, Relatorio

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'CPF', 'login')
@admin.register(CustoFixo)
class CustoFixoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'valor', 'descricao')
    
@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'patrimonio_liquido', 'salario', 'perfil', 'imagem')


@admin.register(DespesasExtras)
class DespesasExtrasAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'valor', 'data')

@admin.register(Investimentos)
class InvestimentosAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'valor_investido', 'rentabilidade', 'investimentos_fisicos')

@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'data', 'conteudo')