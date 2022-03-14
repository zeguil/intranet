from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class MyUserManager(BaseUserManager):
    def create_user(self, cpf, password, **extra_fields):
        if not cpf:
            raise ValueError('Usuário precisa de CPF')

        user = self.model(cpf=cpf, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    

    def create_superuser(self, cpf, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('publisher', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("O superuser deve ter is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("O superuser deve ter is_superuser=True.")
        
        return self.create_user(cpf, password, **extra_fields)

 
class User(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=10,unique=True)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []


    publisher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()
    
    def __str__(self):
        return self.cpf

    @property
    def is_admin(self):
        return self.admin
    
