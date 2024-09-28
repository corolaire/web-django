from django.db import models


class Project(models.Model):
    pass
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100,verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="projects",verbose_name="Imágen")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de Edición")
#upload_to= sube las imagenes al directorio media projects
class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
        def __str__(self):
            return self.title #para que nos aparezca el nombre del proyecto 
         #es para fecha de creación de nuestros registros
# []--- significa que se van a  guardar en una lista las fechas de creacion de los datos
# - ese menos adelante de created hace que se ordenen las fechas y te muestre de los mas actuales a los mas antiguos proyectos.
