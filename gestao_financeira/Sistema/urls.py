from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('gestaoFinanceira/', views.gestaoFinanceira, name='gestaoFinanceira'),
    path('adicionar_custo_fixo/', views.adicionar_custo_fixo, name='adicionar_custo_fixo'),
    path('adicionar_despesa/', views.adicionar_despesa, name='adicionar_despesa'),
    path('remover_custo_fixo/<int:custo_id>/', views.remover_custo_fixo, name='remover_custo_fixo'),
    path('remover_despesa/<int:despesa_id>/', views.remover_despesa, name='remover_despesa'),
]
