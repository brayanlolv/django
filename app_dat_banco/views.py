from django.shortcuts import render
from .models import Usuario
from django.contrib.auth import authenticate    



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
    novo_usuario.save()
    usuarios={'usuarios': Usuario.objects.all()}
    return render(request,'index.html')


def login_tela(request):

    return render(request,'pages/login.html')

def logar(request):
        #logica login
        atualcpf= request.POST.get('cpf')
        atualsenha=request.POST.get('senha')
        

    
        
        
        return render(request,'index.html')


def emprestimo_tela(request):
    return render(request,'pages/emprestimo.html')
    

def cartao(request):
    return render(request,'pages/cartao.html')

def investimento_tela(request):
    return render(request,'pages/investimentos.html')

def poupanca_tela(request):
    return render(request,'pages/poupança.html')

def seguro(request):
    return render(request,'pages/seguro.html')


def transferencia(request):
    return render(request,'pages/tranferencias.html')

def pix(request):
    return render(request,'pages/pix.html')

def pagamento_contas(request):
    return render(request,'pages/pagamento-contas.html')

def cartao(request):
    return render(request,'pages/cartao.html')





