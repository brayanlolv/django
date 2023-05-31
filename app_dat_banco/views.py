from django.shortcuts import render
from .models import Usuario



def home(request):
    return render(request,'index.html')

def cadastro_tela(request):
    return render(request,'pages/cadastro.html')

def cadastro_submit(request):
    novo_usuario = Usuario()
    novo_usuario.nome=request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha=request.POST.get('senha')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.saldo = 0

    return render(request,'index.html')

    novo_usuario.save()

    usuarios={'usuarios': Usuario.objects.all()}

    
    

def cartao(request):
    return render(request,'pages/emprestimo.html')

def investimento_tela(request):
    return render(request,'pages/investimentos.html')

