from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from uuid import uuid4
import os


class AppUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user


class AppUser(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = AppUserManager()
    
    groups = models.ManyToManyField('auth.Group', related_name='app_users')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='app_users')
    
    def __str__(self):
        return self.username


def get_image_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('productos', filename)


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    sigla = models.CharField(max_length=10, default='aaa')
    
    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=250, null=False, blank=False)
    
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    serie = models.CharField(max_length=100, null=False, blank=False)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=False, blank=False)
    codigo = models.CharField(max_length=150)
    descripcion = models.TextField(null=False, blank=False)
    precio = models.DecimalField(max_digits=9, decimal_places=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True        )
    imagen = models.ImageField(upload_to=get_image_filename, null=True, blank=True)


    
    def __str__(self):
        return self.nombre
