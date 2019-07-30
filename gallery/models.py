from django.db import models

class Imagen(models.Model):
   imagen_archivo = models.ImageField(upload_to="gallery")
   nombre_imagen = models.CharField(max_length=200)
   descripcion_imagen = models.TextField()

   def __str__(self):
        return self.nombre_imagen