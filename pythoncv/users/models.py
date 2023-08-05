from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
     email = models.EmailField('correo electronico', unique= True)
     USERNAME_FILED = 'email'
     REQUIRED_FILEDS = ['username']
     
     fotos = models.ImageField( verbose_name = 'foto perfil', upload_to = 'img/usuarios/')
     birthday = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
     Telefono = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
     linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
     perfil_pf = models.TextField(verbose_name='perfil profecional', null=True , blank=True)
     resumen = models.TextField(verbose_name='resumen', null=True , blank=True)
     pais = models.CharField(verbose_name='pais', default='Colombia',max_length=50 )
     ciudad = models.CharField(verbose_name='ciudad', default='Medellín',max_length=50 )
     reclutador = models.BooleanField(verbose_name='reclutador', default=False)
     experiencia = models.BooleanField(verbose_name='experiencia', default=False)
     created = models.DateTimeField(auto_now_add=True, auto_now=False ,null=True , blank=True)
     modified = models.DateTimeField(auto_now_add=True, auto_now=False, null=True , blank = True)
     
