from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from login.models import Profile
from Home.models import fichas
import smtplib
import random

def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        sexo = request.POST['sexo']
        numero = request.POST['telefone']
        if not username.strip():
            print('O campo Username não pode ficar em branco')
            return redirect('cadastro')
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            print('O campo sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=username).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')



        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("looterya@gmail.com", "nwvrsuygdxnkihcr")
        msgFrom = str(email)
        cod = random.randrange(100000,999999)
        msg = "Numero de ativacao da sua conta e {}".format(cod)
        print(msg)
        msgTo = 'looterya@gmail.com'
        assunto = "Confirmacao de email"
        server.sendmail(msgTo,msgFrom,'Subject: {}\n{}'.format(assunto,msg))

        server.quit()
        
        user = User.objects.create_user(username=username, email=email, password=senha,first_name=nome, last_name =sobrenome)  
        user.save() 
        user = auth.authenticate(request, username=username, password=senha)
        auth.login(request, user)

        profile = Profile.objects.create(numero=numero,sexo=sexo,cod_conf=cod,ativado=False,user_id = request.user.id)     
        profile.save()
        print('Usuário cadastrado com sucesso')

        
        return redirect('dashboard')
    else:
        return render(request,'registrar.html')
    return render(request,'registrar.html')

def login(request):
    if request.method == 'POST':
        usuario =  request.POST['usuario']
        senha = request.POST["senha"]
        if usuario == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            print(usuario, senha)
            return render(request,'login.html')
        if User.objects.filter(email=usuario).exists():
            nome = User.objects.filter(email=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            print(nome)
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            print('Login realizado com sucesso')
            return redirect('dashboard')

        return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    
    ficha = fichas.objects.all()
    
    dados={
        'fichas' : ficha
    }
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return redirect('index')
    