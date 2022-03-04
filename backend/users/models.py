from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, cpf, password=None):
     
        if not cpf:
            raise ValueError('O cpf deve ser definido')
        if not password :
            raise TypeError("Defina uma senha")
        user = self.model(cpf=cpf)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, password=None):
        if not cpf:
            raise ValueError('O cpf deve ser definido')
        if not password :
            raise TypeError("Defina uma senha")
        myuser = self.model(cpf=cpf)
        myuser.set_password(password)
        myuser.is_admin = True
        myuser.is_staff = True
        myuser.save()

        return myuser
        

class User(AbstractBaseUser):
    cpf = models.CharField(max_length=10,unique=True)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    publisher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_staff(self):
        return self.admin

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin
    
    def __str__(self):
        return self.cpf

    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
