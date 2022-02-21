
from django.contrib.auth.models import AbstractUser
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Cria e salva um usuário com o e-mail e senha fornecidos.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Cria e salva um usuário da equipe com o e-mail e a senha fornecidos.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Cria e salva um superusuário com o e-mail e a senha fornecidos.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):
    usuario = models.CharField(max_lenght=60, unique=True)
    adm_nome = models.CharField(max_lenght=60)
    senha_hash = models.CharField(128)
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)

    USERNAME_FIELD = 'usuario'
