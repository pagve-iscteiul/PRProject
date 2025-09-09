from django.utils import timezone
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Cliente, Carro
from .models import Questao, Resposta
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.mail import BadHeaderError, send_mail
import os


def Administrador(request):
    return render(request, 'vendas/Administrador.html')

def index(request):
    latest_vendas_list = Carro.objects.all()
    context = {'latest_vendas_list': latest_vendas_list}
    return render(request, 'vendas/index.html', context)

def pesquisa(request):
    marcast= request.POST['marca']
    resultadoCarro=Carro.objects.filter(marca=marcast.lower())
    context = {'resultadoCarro': resultadoCarro}
    return render(request,'vendas/pesquisa.html',context)

def FormularioCompra(request, carro_id):
    c = Carro.objects.get(id=carro_id)
    context = {'carro': c}
    return render(request, 'vendas/FormularioCompra.html', context)

def Carronexiste(request):
    return render(request, 'vendas/CarroNexiste.html')

def pagamentoRemover(request, carro_id):
    envia_email(request, carro_id)
    return render(request, 'vendas/index.html')


def adicionarCarro(request):
    if not request.user.is_superuser:
        return render(request, 'vendas/index.html')
    else:
        return render(request, 'vendas/adicionarCarro.html')

def guardarCarro(request):
    marc = request.POST['marca']
    model = request.POST['modelo']
    matric = request.POST['matricula']
    anoFaric = request.POST['ano_fabrico']
    distpercoric = request.POST['distancia_percorrida']
    prec=request.POST['preco']
    c=Carro(marca=marc,modelo=model,matricula=matric,ano_fabrico=anoFaric,
            distancia_percorrida=distpercoric,preco=prec, imagem=filename)
    c.save()
    return HttpResponseRedirect(reverse('vendas:StoqueCarro'))


def RemoverCarro(request):
    if not request.user.is_superuser:
        return render(request, 'vendas/index.html')
    else:
        return render(request, 'vendas/RemoverCarro.html')

def apagarCarro(request):
    strmarcas = request.POST['matricula']
    if Carro.objects.filter(matricula=strmarcas).exists():
        Carro.objects.get(matricula=strmarcas).delete()
        return HttpResponseRedirect(reverse('vendas:StoqueCarro'))
    else:
        return render(request, 'vendas/CarroNExiste.html')


def StoqueCarro(request):
    resultadoCarro = Carro.objects.all()
    context = {'resultadoCarro': resultadoCarro}
    return render(request, 'vendas/StoqueCarro.html', context)

def about_us(request):
    return render(request, 'vendas/About_US.html')

def how_to_buy(request):
    return render(request, 'vendas/How_to_Buy.html')

def quality(request):
    return render(request, 'vendas/Quality.html')

def spare_parts(request):
    return render(request, 'vendas/Spare_Parts.html')

def contact_us(request):
    return render(request, 'vendas/contactos.html')

def distributors(request):
    return render(request, 'vendas/Distributors.html')

def paginalogin(request):
    return render(request, 'vendas/paginalogin.html')

def loginview(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        u=User.objects.get(username=username)
    except( KeyError, User.DoesNotExist):
        return render(request, 'vendas/paginalogin.html', {'error_messages':'user does not exists'})
    else:
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('vendas:index'), {'notificacao': 'loggin efetuado com sucesso'})
        else:
            return render(request,'vendas/paginalogin.html',{'error_message':'wrong password'})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('vendas:index'),{'sucesso':'sucesso no logout'})

def umaview(request):
    if not request.user.is_authenticated:
        return render(request,'umaapp/login_error.html')

def envia_email(request, carro_id):
    c = Carro.objects.get(id=carro_id)
    destino= request.POST['email_addr']
    apelido = request.POST['SobreNome']
    Assunto="Caro Sr(a)." + apelido + ", enviamos este recibo como forma de confirmar o pagamento do" \
                                      " carro com a Marca:"+ c.marca +" ,Matricula: "+ c.matricula
    send_mail('Recibo do carro', Assunto , settings.EMAIL_HOST_USER , [destino],fail_silently=False)
    Carro.objects.get(id=carro_id).delete()
    return HttpResponseRedirect(reverse('vendas:index'))


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        marc = request.POST['marca']
        model = request.POST['modelo']
        matric = request.POST['matricula']
        anoFaric = request.POST['ano_fabrico']
        distpercoric = request.POST['distancia_percorrida']
        prec = request.POST['preco']
        c = Carro(marca=marc, modelo=model, matricula=matric, ano_fabrico=anoFaric,
                  distancia_percorrida=distpercoric, preco=prec, imagem=filename)
        c.save()
        return render(request,'vendas/index.html',{'uploaded_file_url':   uploaded_file_url})

    return render(request, 'vendas/index.html')

def utilizador(request):
    return render(request, 'vendas/Utilizador.html')

def utilizadorAU(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        #u=User.objects.get(username=username)
        print ('**************** ' +str(user))
        c=Cliente.objects.get(user=user)
        contexto={'util': c}
    except( KeyError, User.DoesNotExist):
        return render(request, 'vendas/paginalogin.html', {'error_messages':'user does not exists'})
    else:
        if user is not None:
            return render(request,'vendas/utilizadorAU.html', contexto)
        else:
            return render(request,'vendas/paginalogin.html',{'error_message':'wrong password'})



def InformacaoUtilizador(request):
    n = request.POST['Nome']
    apel = request.POST['SobreNome']
    emai = request.POST['email_addr']
    morad = request.POST['Morada']
    telef = request.POST['Telefone']
    username = request.POST['username']
    password = request.POST['password']
    use = User.objects.create_user(username,emai,password)
    #use.save()
    c = Cliente(user=use, nome=n, apelido=apel, email=emai, morada=morad,telefone=telef)
    c.save()
    return render(request,'vendas/index.html')


def guardarUtilizador(request):
    nom = request.POST['nome']
    apel = request.POST['sobreNome']
    emai = request.POST['email']
    morad = request.POST['morada']
    telef = request.POST['telefone']
    c = Cliente(nome=nom, apelido=apel, email=emai, morada=morad,
                telefone=telef)
    c.save()
    return HttpResponseRedirect(reverse('vendas:utilizador'))

def paginaregisto(request):
    return render(request, 'vendas/paginaregisto.html')

def alterar(request, cliente_id):
    c = Cliente.objects.get(pk=cliente_id)
    c.nome = request.POST['nome']
    c.apelido = request.POST['SobreNome']
    c.email = request.POST['email_addr']
    c.morada = request.POST['Morada']
    c.telefone = request.POST['Telefone']
    c.save()
    return render(request, 'vendas/n.html', {'cliente': c})

def questao(request):
    latest = Questao.objects.all()
    context = {'perguntas': latest}
    return render(request, 'vendas/questao.html', context)

def guardarQ(request):
    latest = Questao.objects.all()
    context = {'perguntas': latest}
    q = request.POST['questaos']
    respost=Resposta(texto=' ')
    respost.save()
    questao =Questao(questao_texto=q, pub_data=timezone.now(), resposta=respost)
    questao.save()
    return render(request, 'vendas/questao.html', context)

def resposta(request, questao_id):
    latest_question_list = Questao.objects.all()
    context = {'perguntas': latest_question_list}
    q= Questao.objects.get(pk=questao_id)
    r= request.POST['resposta']
    res=Resposta(texto=r)
    q.resposta =res
    res.save()
    return render(request, 'vendas/questao.html', context )

def passaPergResp(request):
 latest_question_list = Questao.objects.all()
 context = {'perguntas': latest_question_list}
 return render(request, 'vendas/.html', context)


