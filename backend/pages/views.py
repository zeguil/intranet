
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
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404

from banner.models import Banner
from banner.serializers import BannerSerializer

from comentario.models import Comentario
from audit.models import Audit
from audit.serializers import AuditSerializer
from corporativo.models import Corporativo
from corporativo.serializers import CorporativoSerializer
from emails.models import Email
from emails.serializers import EmailSerializer
from funcionario.models import Funcionario
from funcionario.serializers import FuncionarioSerializer

from informativo.models import Informativo
from informativo.serializers import InformativoSerializer
from ramal.models import Ramal
from ramal.serializers import RamalSerializer
from setor.models import Setor
from setor.serializers import SetorSerializer




    

class Noticias(APIView):
    def get(self, request, id):
        try:
            banner = Banner.objects.get(pk=id)
            serializer = BannerSerializer(banner)

        except Banner.DoesNotExist:
            raise Http404("Banner não encontrado....")

        return Response(serializer.data)



class Nivers(APIView):
    def get(self, request):

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

        funcs = Funcionario.objects.select_related('setor_id').filter(
            mes_nasc__exact=busca, state__exact= 0).order_by('dia_nasc')

        serializer_func = FuncionarioSerializer(funcs)

        dados = {
            'funcionario': serializer_func.data,
            'title': 'Aniversariantes',
            'busca': busca,
            'dia': dia,
            'plus': dia_plus
        }

        return Response(dados)


class Info(APIView):
    def get(self, request):
        infos = Informativo.objects.filter(state__exact=0).order_by('id').desc()[:8]
        serializer = InformativoSerializer(infos)

        return Response(serializer.data)

class Ramais(APIView):
    def get(self, request):

        ramais = Ramal.objects.select_related('setor_id').filter(
        state__exact=0).order_by(Setor.rank, 'rank'),
        corps = Corporativo.objects.select_related('setor_id').filter(
        state__exact= 0).order_by('rank'),
        mails = Email.objects.filter().order_by('id')

        serializer_ramais = RamalSerializer(ramais)
        serializer_corps = CorporativoSerializer(corps)
        serializer_mails = EmailSerializer(mails)

        dados = {
            'ramais': serializer_ramais.data,
            'corporativos' : serializer_corps.data,
            'emails': serializer_mails.data
        }
        

        return Response(dados)

class Mural(APIView):
    def get(self, request, id):


        coments = Comentario.objects.filter(func_id__exact = id, ano__exact = datetime.today(
        ).year, state__exact = 0).order_by('id').desc()

        func = get_object_or_404(Funcionario, pk=id)

        nome = func.func_nome.strip()

        nome = nome.split(' ')[0] + ' ' + nome.split(' ')[-1]

        nome = nome.title()

        dados = {
            "coments": coments,
            "nome": nome,
            "date": datetime
        }
        return dados

    def post(request):


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

    




