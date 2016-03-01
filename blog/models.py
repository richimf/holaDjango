
# *-------> Definimos los objetos llamados Models, aqui definiremos nuestro
# modelo de post

from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model): #heredamos de la clase base Model, esto es un modelo y django sabe que debe guardaro en la BD
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self): # Usamos un "dunder" o dobles guiones bajos
            return self.title

    # Asi definimos una Clase
    #    class MiClase

    # Asi definimos una funcion
        # def mi_funcion():
            # aqui mi algoritmo
            # return mi_valor

    # Asi invocamos la funcion
        # mi_funcion()

    # Asi definimos una funcion con parametros
        # def mi_funcion(parametro1,parametro2):

    # Asi definimos una funcion con parametros por omision
        # def mi_funcion(parametro1, parametro2 = "hola"):

    # Asi invocamos la funcion
        # mi_funcion(valor=555, valor="hola que hace")
