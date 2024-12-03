from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('gestaoFinanceira/', views.gestaoFinanceira, name='gestaoFinanceira'),
    path('adicionar_custo_fixo/', views.adicionar_custo_fixo, name='adicionar_custo_fixo'),
    path('adicionar_despesa/', views.adicionar_despesa, name='adicionar_despesa'),
]
