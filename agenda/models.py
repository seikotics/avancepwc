from django.db import models
from django.urls import reverse
# Create your models here.
class Agenda(models.Model):
    titulo_agenda = models.CharField (max_length = 50, primary_key = True)
    bajada_titulo_agenda = models.CharField(max_length = 50)
    texto_agenda = models.TextField()
    imagen_agenda = models.ImageField(upload_to="static")
    imagen_agenda_dos = models.ImageField(upload_to="static")
    fechapublicacion_agenda = models.DateTimeField()
       # HERE 
    def __str__(self):
        return'%s %s'%(self.titulo_agenda,self.fechapublicacion_agenda)
