from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
     TYPE_ID =[
        ("Registro Civil", "Registro Civil"),
        ("Tarjeta de Identidad", "Tarjeta de Identidad"),
        ("Cédula de Ciudadanía", "Cédula de Ciudadanía"),
        ("Cédula de Extranjería", "Cédula de Extranjería"),
        ("Pasaporte", "Pasaporte"),
        ("Permiso Temporal", "Permiso Temporal"),
     ]  


     email = models.EmailField('correo electronico', unique= True)
     USERNAME_FILED = 'email'
     REQUIRED_FILEDS = ['username']
     

     type_id = models.CharField(verbose_name='Tipo de identificacion')
     identification = models.CharField(verbose_name='Número de Identificación', max_length=50)
     photos = models.ImageField( verbose_name = 'foto perfil', upload_to = 'img/usuarios/')
     country_avaliable = models.CharField(verbose_name='Pais de Residencia', max_length=200)
     city_avaliable = models.CharField( verbose_name='Ciudad de Residencia' , max_length=200 )
     adress = models.TextField(verbose_name='Direccion de Recidencia')
     phone = models.CharField(verbose_name='Teléfono', max_length=20, null=True, blank=True)
     birthday = models.DateField(verbose_name="Fecha de Nacimiento", null=True, blank=True)
     occupation_jop = models.CharField(verbose_name='Ocupacion', max_length=150)
     relocate = models.BooleanField('disponibilidad para desplasarze', default=False)
     is_recruiter = models.BooleanField('reclutador', default=False)
     created = models.DateTimeField(auto_now_add=True, auto_now=False )
     modified = models.DateTimeField(auto_now=True, auto_now=False)


class link(models.Model):
      
      TYPE_LINK =[
            ("Repositorio", "Repositorio"),
            ("LinkedIN", "LinkedIN"),
            ("WebSite", "WebSite"),
            ("Red Social", "Red Social"),
       ]

      user = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
      type_link = models.CharField(verbose_name='Tipo de Enlace', max_length=50 ,choices=TYPE_LINK)
      link_url =models.URLField(verbose_name='Link')
      created = models.DateTimeField( auto_now_add=True)
      modified = models.DateTimeField( auto_now=True)

      class meta:
            verbose_name ="Enlace"
            verbose_name_plural = "Enlaces"

      def __str__(self):
            return f'(self.link_url)'
      
class ResumenUser(models.Model):      
     RESUME_SECCION = [
            ("PP", "Perfil Profesional"),
            ("RR", "Resumen Profesional"),
            ("RF", "Resume Hechos"),
            ("RS", "Resumen Sumario"),
            ("RA", "Resumen Adjetivos"),
            ("RC", "Resumen Contacto"),
     ]
 
     type_resume = models.CharField(verbose_name='Tipo de Resumen', max_length=20, choices=RESUME_SECCION)
     resumes = RichTextField(verbose_name='Resumen')
     created = models.DateTimeField(auto_now_add=True)
     modified = models.DateTimeField(auto_now=True)

     class Meta:
        verbose_name ="Resumen"
        verbose_name_plural ="Resumenes"

     def __str__(self):
        return f'{self.type_resume}'