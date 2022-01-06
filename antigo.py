from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from datetime import datetime


class Administrador(UserMixin, models.Model):


    usuario = models.CharField(max_length=60, index=True, unique=True)
    adm_nome = models.CharField(max_length=60, index=True)
    senha_hash = models.CharField(max_length=128)
    is_admin = db.Column(db.Boolean, default=False)
    is_publisher = db.Column(db.Boolean, default=False)
    info = db.relationship(
        'Informativo', backref='administrador', lazy='dynamic')

    @property
    def senha(self):

        raise AttributeError('Senha não pode ser lida.')

    @senha.setter
    def senha(self, senha):

        self.senha_hash = generate_password_hash(senha)

    def verify_password(self, senha):

        return check_password_hash(self.senha_hash, senha)

    def __str__(self):
        return f'<Administrador: {self.usuario}>'


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Administrador.query.get(int(user_id))


class Ramal(models.Model):

    
    subsetor = models.CharField(max_length=60)
    responsavel = models.CharField(max_length=120)
    ramal = models.CharField(max_length=20)
    setor_id = models.ForeignKey(Setor)
    state = models.IntegerField(default=0)
    isBoss = moedls.BooleanField(default=False, null=True)
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f'<Ramal: {self.id}>'


class Informativo(models.Model):

    titulo = models.CharField(max_length=60)
    link = models.CharField(max_length=240)
    image = models.CharField(max_length=50)
    data_pub = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)
    admin_id = models.ForeignKey('administradores.id')

    def __str__(self):
        return f'<Informativo: {self.titulo}>'


class Funcionario(models.Model):

    func_nome = models.CharField(max_length=60, index=True)
    dia_nasc = models.IntegerField()
    mes_nasc = models.CharField(20)
    setor_id = models.ForeignKey(Setor)
    state = models.IntegerField(default=0)
    comentario = db.relationship(
        'Comentario', backref='funcionario', lazy='dynamic')

    def __str__(self):
        return f'<Funcionario: {self.func_nome}>'


class Comentario(models.Model):

    com_nome = models.CharField(max_length=60, index=True)
    conteudo = models.TextField()
    ano = models.IntegerField(default=datetime.today().year)
    data_env = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)
    func_id = models.ForeignKey(Funcionario)

    def __str__(self):
        return f'<Comentario: {self.com_nome}>'


class Audit(models.Model):
   
    tabela = models.CharField(max_length=60)
    createdon = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=60)
    action = models.CharField(max_length=240)
    hostname = models.CharField(max_length=60)
    usuario = models.CharField(max_length=60)
    id_tab = models.IntegerField()

    def __str__(self):
        return f'<Audit: {self.id}>'


class Setor(models.Model):

    
    set_nome = models.CharField(max_length=60, index=True)
    state = models.IntegerField(default=0)
    ramal = db.relationship('Ramal', backref='setor', lazy='dynamic')
    corporativo = db.relationship(
        'Corporativo', backref='setor', lazy='dynamic')
    func = db.relationship('Funcionario', backref='setor', lazy='dynamic')
    rank = models.IntegerField(null=True)

    def __str__(self):
        return f'<Setor: {self.set_nome}>'


class Corporativo(models.Model):

    
    imei = models.CharField(max_length=240)
    marca = models.CharField(max_length=60)
    modelo = models.CharField(max_length=60)
    numero = models.CharField(max_length=60)
    nome = models.CharField(max_length=60)
    setor_id = models.ForeignKey('setor.id')
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'<Corporativo: {self.id}>'


class Email(models.Model):

    email = models.CharField(max_length=)
    responsavel = models.CharField(max_length=)

    def __str__(self):
        return f'<Email: {self.id}>'


class Banner(models.Model):

    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    hasPage = models.BooleanField(default=False)
    image = models.CharField(max_length=50)
    data_pub = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(default=0)
    ordem = models.IntegerField(null=True)
    link_externo = models.CharField(max_length=255)

    def __str__(self):
        return f'<Banner: {self.titulo}>'
