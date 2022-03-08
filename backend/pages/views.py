
# from . import home
# from .forms import FormularioMural

import requests

import socket
import os
from bs4 import BeautifulSoup
from datetime import datetime
from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

from banner.models import Banner
from comentario.models import Comentario
from audit.models import Audit
from corporativo.models import Corporativo
from emails.models import Email
from funcionario.models import Funcionario
from informativo.models import Informativo
from ramal.models import Ramal
from setor.models import Setor



@api_view(["POST", "GET"]) 
@permission_classes([AllowAny]) 
def homepage(request):

    try:
        
        r = requests.get('http://imprensaoficial.am.gov.br/')
        
        print(r)
        status = r.status_code

        if status == 200:

            soup = BeautifulSoup(r.content, "html.parser")

            news = soup.find_all('section', {'class': 'container noticias'})[
                0].find_all('article')

            imgs = soup.find_all('figure', {'class': 'pinterest'})

        else:

            news = ''
            imgs = ''

    except requests.exceptions.ConnectionError or requests.exceptions.Timeout or requests.exceptions.RequestException or requests.exceptions.TooManyRedirects or requests.exceptions.HTTPError:

        status = 404

        news = ''
        imgs = ''

    hoje = datetime.today()
    mes = hoje.month
    dia = hoje.day

    hasModal = True if hoje.date() == datetime(2021, 11, 17).date() else False

    if mes == 1:
        busca = 'Janeiro'
    elif mes == 2:
        busca = 'Fevereiro'
    elif mes == 3:
        busca = 'Março'
    elif mes == 4:
        busca = 'Abril'
    elif mes == 5:
        busca = 'Maio'
    elif mes == 6:
        busca = 'Junho'
    elif mes == 7:
        busca = 'Julho'
    elif mes == 8:
        busca = 'Agosto'
    elif mes == 9:
        busca = 'Setembro'
    elif mes == 10:
        busca = 'Outubro'
    elif mes == 11:
        busca = 'Novembro'
    elif mes == 12:
        busca = 'Dezembro'

    if hoje.weekday() == 4:

        plus = dia + 2

        funcs = Funcionario.objects.filter(Funcionario.mes_nasc == busca, Funcionario.dia_nasc >= dia,
                                         Funcionario.dia_nasc <= plus, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

        print(funcs)
    else:

        funcs = Funcionario.objects.filter(Funcionario.mes_nasc == busca, Funcionario.dia_nasc ==
                                         dia, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

    if funcs:
        niver = True
    else:
        niver = False

    banners = Banner.objects.filter(
        Banner.state == 0).order_by(Banner.ordem, Banner.data_pub.desc()).all()

    bannersPath = '../static/images/banners/'

    data = {
        'title':"Imprensa Oficial IntraNet",
        'news': news,
        'imgs':imgs,
        'status':status,
        'niver':niver,
        'mes':busca,
        'banners':banners,
        'bannersPath':bannersPath,
        'hasModal':hasModal
    }

    return data


@api_view(["GET"]) 
@permission_classes([AllowAny]) 
def ramais(request):

    ramais = Ramal.objects.join(Setor).filter(
        Ramal.state == 0).order_by(Setor.rank, Ramal.rank).all()
    corps = Corporativo.objects.join(Setor).filter(
        Corporativo.state == 0).order_by(Setor.rank).all()
    mails = Email.objects.filter().order_by(Email.id).all()

    return render('home/ramais.html', corps=corps, ramais=ramais, mails=mails, title="Ramais")


@api_view(["GET"]) 
@permission_classes([AllowAny]) 
def nivers(request):

    hoje = datetime.today()
    mes = hoje.month
    dia = hoje.day

    if mes == 1:
        busca = 'Janeiro'
    elif mes == 2:
        busca = 'Fevereiro'
    elif mes == 3:
        busca = 'Março'
    elif mes == 4:
        busca = 'Abril'
    elif mes == 5:
        busca = 'Maio'
    elif mes == 6:
        busca = 'Junho'
    elif mes == 7:
        busca = 'Julho'
    elif mes == 8:
        busca = 'Agosto'
    elif mes == 9:
        busca = 'Setembro'
    elif mes == 10:
        busca = 'Outubro'
    elif mes == 11:
        busca = 'Novembro'
    elif mes == 12:
        busca = 'Dezembro'

    if hoje.weekday() == 4:
        dia_plus = dia + 2
    else:
        dia_plus = dia

    funcs = Funcionario.objects.join(Setor).filter(
        Funcionario.mes_nasc == busca, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

    return render('home/aniversariantes.html', funcs=funcs, title="Aniversariantes", str=str, busca=busca, dia=dia, plus=dia_plus)


@api_view(["GET"]) 
@permission_classes([AllowAny]) 
def info(request):

    infos = Informativo.objects.filter(Informativo.state == 0).order_by(
        Informativo.id.desc()).limit(8).all()

    return render('home/informativos.html', infos=infos, title='Informativos')


@api_view(["POST","GET"]) 
@permission_classes([AllowAny]) 
def mural(id):

    coments = Comentario.objects.filter(Comentario.func_id == id, Comentario.ano == datetime.today(
    ).year, Comentario.state == 0).order_by(Comentario.id.desc()).all()

    func = Funcionario.objects.get_or_404(id)

    nome = func.func_nome.strip()

    nome = nome.split(' ')[0] + ' ' + nome.split(' ')[-1]

    nome = nome.title()

    form = FormularioMural()

    if form.validate_on_submit(request):

        com_add = Comentario(
            com_nome=form.nome.data, conteudo=form.conteudo.data, func_id=id, data_env=datetime.now())

        ip = frq.environ.get('HTTP_X_REAL_IP', frq.remote_addr)
        user = frq.remote_user

        try:
            db.session.add(com_add)
            db.session.flush()

            audit = Audit(tabela='COMENTARIO', ip=ip, action='INSERT', hostname=socket.getfqdn(
                ip), usuario=user, createdon=datetime.now(), id_tab=com_add.id)
            db.session.add(audit)
            db.session.commit()

            flash('Mensagem enviada!')

        except:
            raise('Error: Não foi possível enviar a mensagem!')

        return redirect('home.mural', id=func.id)

    return render('home/mural.html', form=form, coments=coments, nome=nome, date=datetime)

# @api_view(["GET"]) 
# @permission_classes([AllowAny])
# def redirects(id):

#     info = Informativo.objects.get_or_404(id)

#     ip = frq.environ.get('HTTP_X_REAL_IP', frq.remote_addr)

#     user = frq.remote_user

#     audit = Audit(tabela='REDIRECT', ip=ip, action=info.link, hostname=socket.getfqdn(
#         ip), usuario=user, createdon=datetime.now(), id_tab=info.id)

#     db.session.add(audit)

#     db.session.commit()

#     return render('home/redirect.html', info=info)

@api_view(["GET"]) 
@permission_classes([AllowAny])
def noticias(id): #noticias/<id>

    banner = Banner.objects.get_or_404(id)

    return render('home/noticia.html', banner=banner)


