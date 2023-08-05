from django.db import models
from users.models import User
from choices.choices import Estudios,Nivel

# Create your models here.

class tecnologias(models.Model):
    nombre_tecnologia = models.CharField(verbose_name = 'nombre tecnologia', max_length=100 )
    created = models.DateTimeField(verbose_name='creado :'  ,auto_now_add=True, auto_now=False ,null=True , blank=True)
    modified = models.DateTimeField( verbose_name= 'modificado : ',auto_now_add=True, auto_now=False, null=True , blank = True)
   
    class meta:
        verbose_name = 'tecnologia'      
        verbose_name_plural = 'tecnologias'

    def __str__(self):
         return f'{self.nombre_tecnologia}'   


class proyectos_laborales(models.Model):
     nombre = models.CharField(verbose_name = 'Nombre de proyecto', max_length = 50)
     link = models.URLField(verbose_name='link  de proyecto', max_length = 100 ) 
     Tecnologia = models.CharField(verbose_name='tecnologia utilizada', max_length=100)
     fecha_creacion = models.DateField(verbose_name = 'fecha de terminacion', blank = True , null = True)
     descripcion = models.TextField(verbose_name='descripcion de proyecto')
     id_user = models.ForeignKey(User,on_delete=models.CASCADE)
     created = models.DateTimeField(verbose_name='creado :'  ,auto_now_add=True, auto_now=False ,null=True , blank=True)
     modified = models.DateTimeField( verbose_name= 'modificado : ',auto_now_add=True, auto_now=False, null=True , blank = True)
     
     class meta:
        verbose_name = 'proyectos desarrollado'      
        verbose_name_plural = 'proyectos desarrollados'

     def __str__(self):
         return f'{self.nombre} {self.link}' 

     
class experiencia_laboral(models.Model):
      experiencia = models.BooleanField(verbose_name='experiencia', default=False)
      empresa = models.CharField(max_length=100)
      cargo  = models.CharField(max_length=100)
      descripcion = models.TextField(verbose_name='descripcionde proyecto')
      fecha_inicio = models.DateField()
      fecha_fin = models.DateField(null=True , blank=True )
      id_user = models.ForeignKey(User,on_delete=models.CASCADE)
      created = models.DateTimeField(verbose_name='creado:',auto_now_add=True, auto_now=False ,null=True , blank=True)
      modified = models.DateTimeField(verbose_name='modificado:',auto_now_add=True, auto_now=False, null=True , blank = True)
      
      class meta:
        verbose_name = 'experiencia laboral'      
        verbose_name_plural = 'experiencia laborales'

      def __str__(self):
         return f'{self.cargo}-{self.empresa}' 

class Estudios(models.Model):
      estudio = models.CharField(verbose_name='tipo de estudio', choices=Estudios , max_length=100)
      titulo = models.CharField(verbose_name='titulo obtenido', max_length=100)
      institucion = models.CharField(max_length=100)
      descripcion = models.TextField()
      cursando = models.BooleanField(verbose_name='en curso', default=True)
      fecha_fin = models.DateField(null=True , blank=True )
      id_user = models.ForeignKey(User,on_delete=models.CASCADE)
      created = models.DateTimeField(verbose_name='creado :',auto_now_add=True, auto_now=False ,null=True , blank=True)
      modified = models.DateTimeField(verbose_name='modificado :',auto_now_add=True, auto_now=False, null=True , blank = True)
      
      class meta:
        verbose_name = 'estudio'      
        verbose_name_plural = 'estudios'

      def __str__(self):
         return self.titulo


class hobbies(models.Model):
      hobbies = models.CharField(verbose_name='hobbies', max_length=100)
      id_user = models.ForeignKey(User,on_delete=models.CASCADE)
      created = models.DateTimeField(verbose_name='creado :',auto_now_add=True, auto_now=False ,null=True , blank=True)
      modified = models.DateTimeField(verbose_name='modificado :',auto_now_add=True, auto_now=False, null=True , blank = True)
      

      class meta:
        verbose_name = 'hobbi'      
        verbose_name_plural = 'hobbies'

      def __str__(self):
         return self.hobbies


class habilidades(models.Model):
      habilidad = models.CharField(verbose_name='Competencias', max_length=100)
      nivel = models.CharField(verbose_name= 'Nivel', max_length=100 , choices=Nivel)
      id_user = models.ForeignKey(User,on_delete=models.CASCADE)
      created = models.DateTimeField(verbose_name='creado :',auto_now_add=True, auto_now=False ,null=True , blank=True)
      modified = models.DateTimeField(verbose_name='modificado :',auto_now_add=True, auto_now=False, null=True , blank = True)


      class meta:
        verbose_name = 'habilidad'  
        verbose_name_plural = 'habilidades'

      def __str__(self):
         return f'{self.habilidad}'