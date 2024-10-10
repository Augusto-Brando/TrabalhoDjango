import uuid
from django.db import models
from django.core.exceptions import ValidationError
from stdimage.models import StdImageField
from django.utils.translation import gettext_lazy as _

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

# Usuário
class Usuario(models.Model):
    CPF = models.CharField(_('CPF'), max_length=11, unique=True, primary_key=True)
    nome = models.CharField(_('Nome'), max_length=100)
    login = models.CharField(_('Login'), max_length=100)
    senha = models.CharField(_('Senha'), max_length=100)

    def clean(self):
        if not self.nome or not self.login or not self.senha:
            raise ValidationError(_("Todos os campos de usuário são obrigatórios."))

    def __str__(self):
        return f'Usuário: {self.nome} - CPF: {self.CPF}'

    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

# Perfil de Usuário
class PerfilUsuario(models.Model):
    PERFISINVESTIMENTOS = [
    ('Conservador', _('Conservador')),
    ('Moderado', _('Moderado')),
    ('Arrojado', _('Arrojado')),
    ('Agressivo', _('Agressivo')),
    ('Balanceado', _('Balanceado')),
]
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    patrimonio_liquido = models.DecimalField(_('Patrimônio Líquido'), max_digits=15, decimal_places=2)
    salario = models.DecimalField(_('Salário'), max_digits=10, decimal_places=2)
    dividas = models.DecimalField(_('Dívidas'), max_digits=15, decimal_places=2)
    metas = models.TextField(_('Metas'), null=True, blank=True)
    perfil = models.CharField(_('Perfil'),choices=PERFISINVESTIMENTOS, max_length=50)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path, null=True, blank=True, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})

    def __str__(self):
        return f'Perfil do Usuário: {self.usuario.nome}'

    class Meta:
        verbose_name = _('Perfil de Usuário')
        verbose_name_plural = _('Perfis de Usuário')

# Custo Fixo
class CustoFixo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    descricao = models.CharField(_('Descrição'), max_length=255)

    def __str__(self):
        return f'Custo Fixo: {self.descricao} - Valor: {self.valor}'

    class Meta:
        verbose_name = _('Custo Fixo')
        verbose_name_plural = _('Custos Fixos')

# Despesa Extra
class DespesasExtras(models.Model):
    TIPOS = [
        ('Comida', _('Comida')),
        ('Festas', _('Festas')),
        ('Passeios', _('Passeios')),
        ('Educação', _('Educação')),
        ('Transporte', _('Transporte')),
        ('Saúde', _('Saúde')),
        ('Lazer', _('Lazer')),
        ('Outros', _('Outros')),
    ]
    usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    tipo = models.CharField(_('Tipo de Despesa'), max_length=50, choices=TIPOS, default='Outros')
    valor = models.DecimalField(_('Valor'), max_digits=10, decimal_places=2)
    data = models.DateField(_('Data'),null=True, blank=True)

    def __str__(self):
        return f'Despesa Extra: {self.get_tipo_display()} - Valor: {self.valor}'
    
    class Meta:
        verbose_name = _('Despesa Extra')
        verbose_name_plural = _('Despesas Extras')

# Investimentos
class Investimentos(models.Model):
    TIPOSINVESTIMENTOS = [
    ('Fundos', _('Fundos')),
    ('Ações', _('Ações')),
    ('Tesouro', _('Tesouro')),
    ('CDB', _('CDB')),
    ('Imóveis', _('Imóveis')),
    ('Criptomoedas', _('Criptomoedas')),
    ('Previdência Privada', _('Previdência Privada')),
    ('Outros', _('Outros')),
]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(_('Tipo de Investimento'), max_length=50, choices=TIPOSINVESTIMENTOS, default='Outros')
    valor_investido = models.DecimalField(_('Valor Investido'), max_digits=15, decimal_places=2)
    rentabilidade = models.DecimalField(_('Rentabilidade'), max_digits=5, decimal_places=2)
    investimentos_fisicos = models.TextField(_('Investimentos Físicos'), null=True, blank=True)

    def __str__(self):
        return f'Investimento: {self.tipo} - Valor: {self.valor_investido}'

    class Meta:
        verbose_name = _('Investimento')
        verbose_name_plural = _('Investimentos')

# Relatório
class Relatorio(models.Model):
    TIPOSRELATORIOS = [
    ('Mensal', _('Mensal')),
    ('Trimestral', _('Trimestral')),
    ('Semestral', _('Semestral')),
    ('Anual', _('Anual'))
]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(_('Tipo de Relatório'),choices=TIPOSRELATORIOS, max_length=50)
    data = models.DateField(_('Data'))
    conteudo = models.TextField(_('Conteúdo'), null=True, blank=True)

    def __str__(self):
        return f'Relatório: {self.tipo} - Data: {self.data}'

    class Meta:
        verbose_name = _('Relatório')
        verbose_name_plural = _('Relatórios')