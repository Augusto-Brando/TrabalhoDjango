from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as login_django
import re
from .models import CustoFixo, Despesa, Investimento
from django.db.models import Sum
from decimal import Decimal

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verificação de CPF
        if not re.match(r'^\d{11}$', cpf):  # Verifica se o CPF tem apenas 11 dígitos numéricos
            return render(request, 'cadastro.html', {'error': 'CPF inválido. Deve conter apenas números e ter 11 dígitos.'})

        if User.objects.filter(username=cpf).exists():  # Verifica se o CPF já está cadastrado
            return render(request, 'cadastro.html', {'error': 'Este CPF já está cadastrado.'})

        # Verificação de Email
        if User.objects.filter(email=email).exists():  # Verifica se o email já está cadastrado
            return render(request, 'cadastro.html', {'error': 'Este email já está cadastrado.'})

        # Verificação de senhas iguais
        if senha != confirmar_senha:
            return render(request, 'cadastro.html', {'error': 'As senhas não são iguais.'})

        # Criação do usuário
        user = User.objects.create_user(username=cpf, email=email, password=senha)
        user.first_name = nome
        user.last_name = sobrenome
        user.save()

        return HttpResponse('Usuário cadastrado com sucesso!')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        # Verifica a autenticação do usuário
        user = authenticate(username=cpf, password=senha)

        if user:
            login_django(request, user)
            return redirect('gestaoFinanceira')  # Redirecionamento correto para a página de gestão financeira
        else:
            # Passa a mensagem de erro para o template
            return render(request, 'login.html', {'error': 'CPF ou senha inválidos.'})
        

@login_required
def gestaoFinanceira(request):
    custos_fixos = CustoFixo.objects.filter(usuario=request.user)
    despesas = Despesa.objects.filter(usuario=request.user)
    investimentos = Investimento.objects.filter(usuario=request.user).order_by('id')  # Adicionando a busca dos investimentos

    # Cálculos dos totais
    total_custos_fixos = sum(c.valor for c in custos_fixos)
    total_despesas = sum(d.valor for d in despesas)

    return render(request, 'gestaoFinanceira.html', {
        'custos_fixos': custos_fixos,
        'despesas': despesas,
        'total_custos_fixos': total_custos_fixos,
        'total_despesas': total_despesas,
        'investimentos': investimentos  # Passando os investimentos para o template
    })

@login_required
def adicionar_custo_fixo(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        CustoFixo.objects.create(usuario=request.user, descricao=descricao, valor=valor)
        return redirect('gestaoFinanceira')
    return render(request, 'adicionar_custo_fixo.html')

@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        Despesa.objects.create(usuario=request.user, descricao=descricao, valor=valor)
        return redirect('gestaoFinanceira')
    return render(request, 'adicionar_despesa.html')

@login_required
def remover_custo_fixo(request, custo_id):
    custo_fixo = get_object_or_404(CustoFixo, id=custo_id, usuario=request.user)
    custo_fixo.delete()
    return redirect('gestaoFinanceira')

@login_required
def remover_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, id=despesa_id, usuario=request.user)
    despesa.delete()
    return redirect('gestaoFinanceira')

@login_required
def adicionar_investimento(request, investimento_id):
    investimento = get_object_or_404(Investimento, id=investimento_id)

    if request.method == 'POST':
        valor = request.POST.get('valor')

        # Atualizando o valor do investimento
        investimento.valor += Decimal(valor)  # Supondo que você queira somar o valor
        investimento.save()

        return redirect('gestaoFinanceira')  # Redireciona de volta para a página principal de gestão financeira

    return redirect('gestaoFinanceira')  # Caso o método não seja POST

