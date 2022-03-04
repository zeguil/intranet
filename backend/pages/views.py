
from . import home
from .forms import FormularioMural

import requests
from requests.exceptions import Timeout
import socket
import os
from bs4 import BeautifulSoup
from datetime import datetime

from banner.models import Banner
from comentario.models import Comentario
from audit.models import Audit
from corporativo.models import Corporativo
from emails.models import Email
from funcionario.models import Funcionario
from informativo.models import Informativo
from ramal.models import Ramal
from setor.models import Setor

# @api_view(["POST"]) 
# @permission_classes([AllowAny]) 
# def Register_Users(request): 
#     try: 
#         data = [] 
#         serializer = RegistrationSerializer(data=request.data) 
#         if serializer.is_valid(): 
#             account = serializer.save () 
#             account.is_active = True 
#             account.save() 
#             token = Token.objects.get_or_create(user=account)[0].key 
#             data["message"] = "usuário registrado com sucesso" 
#             data["email"] = conta. email 
#             data["username"] = account.username 
#             data["token"] = token 

#         else: 
#             data = serializer.erros 


@home.route('/', methods=['GET', 'POST'])
def homepage():

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

        funcs = Funcionario.query.filter(Funcionario.mes_nasc == busca, Funcionario.dia_nasc >= dia,
                                         Funcionario.dia_nasc <= plus, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

        print(funcs)
    else:

        funcs = Funcionario.query.filter(Funcionario.mes_nasc == busca, Funcionario.dia_nasc ==
                                         dia, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

    if funcs:
        niver = True
    else:
        niver = False

    banners = Banner.query.filter(
        Banner.state == 0).order_by(Banner.ordem, Banner.data_pub.desc()).all()

    bannersPath = '../static/images/banners/'

    return render_template('home/index.html', title="Imprensa Oficial IntraNet", news=news, imgs=imgs, status=status, niver=niver, mes=busca, banners=banners, bannersPath=bannersPath, hasModal=hasModal)


@home.route('/ramais')
def ramais():

    ramais = Ramal.query.join(Setor).filter(
        Ramal.state == 0).order_by(Setor.rank, Ramal.rank).all()
    corps = Corporativo.query.join(Setor).filter(
        Corporativo.state == 0).order_by(Setor.rank).all()
    mails = Email.query.filter().order_by(Email.id).all()

    return render_template('home/ramais.html', corps=corps, ramais=ramais, mails=mails, title="Ramais")


@home.route('/dashboard')
@login_required
def dashboard():

    return render_template('home/dashboard.html', title="Admin Dashboard")


@home.route('/nivers')
def nivers():

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

    funcs = Funcionario.query.join(Setor).filter(
        Funcionario.mes_nasc == busca, Funcionario.state == 0).order_by(Funcionario.dia_nasc).all()

    return render_template('home/aniversariantes.html', funcs=funcs, title="Aniversariantes", str=str, busca=busca, dia=dia, plus=dia_plus)


@home.route('/info')
def info():

    infos = Informativo.query.filter(Informativo.state == 0).order_by(
        Informativo.id.desc()).limit(8).all()

    return render_template('home/informativos.html', infos=infos, title='Informativos')


@home.route('/mural/<int:id>', methods=['GET', 'POST'])
def mural(id):

    coments = Comentario.query.filter(Comentario.func_id == id, Comentario.ano == datetime.today(
    ).year, Comentario.state == 0).order_by(Comentario.id.desc()).all()

    func = Funcionario.query.get_or_404(id)

    nome = func.func_nome.strip()

    nome = nome.split(' ')[0] + ' ' + nome.split(' ')[-1]

    nome = nome.title()

    form = FormularioMural()

    if form.validate_on_submit():

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
            flash('Error: Não foi possível enviar a mensagem!')

        return redirect(url_for('home.mural', id=func.id))

    return render_template('home/mural.html', form=form, coments=coments, nome=nome, date=datetime)


@home.route('/sistemas', methods=['GET'])
def sistemas():

    return render_template('home/sistemas.html')


@home.route('/redirect/<int:id>', methods=['GET'])
def redirects(id):

    info = Informativo.query.get_or_404(id)

    ip = frq.environ.get('HTTP_X_REAL_IP', frq.remote_addr)

    user = frq.remote_user

    audit = Audit(tabela='REDIRECT', ip=ip, action=info.link, hostname=socket.getfqdn(
        ip), usuario=user, createdon=datetime.now(), id_tab=info.id)

    db.session.add(audit)

    db.session.commit()

    return render_template('home/redirect.html', info=info)


@home.route('/id-am', methods=['GET'])
def certifica_id():

    return render_template('home/certifica-id-ioa.html')


@home.route('/certifica', methods=['GET'])
def certifica_id_amazonprev():

    return render_template('home/certifica-id-amazonprev.html')


@home.route('/qrcode', methods=['GET'])
def qrcode():

    return render_template('home/qrcode.html')


@home.route('/manuais', methods=['GET'])
def manuais():

    return render_template('home/manuais.html')


@home.route('/manuais/siged', methods=['GET'])
def siged():

    return render_template('home/manuais/siged.html')


@home.route('/noticias/<int:id>', methods=['GET'])
def noticias(id):

    banner = Banner.query.get_or_404(id)

    return render_template('home/noticia.html', banner=banner)


@home.route('/live', methods=['GET'])
def live():
    return render_template('home/live.html')
