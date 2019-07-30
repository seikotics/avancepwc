from django.db import models

class Noticia(models.Model):
    titulo = models.CharField (max_length = 50, primary_key = True)
    autor = models.CharField(max_length = 50)
    bajada_titulo = models.CharField(max_length = 50)
    texto = models.TextField()
    imagenes = models.ImageField(upload_to="static")
    fechapublicacion = models.DateTimeField()
       # HERE 
    def __str__(self):
        return'%s %s'%(self.titulo,self.fechapublicacion)

class Comentario(models.Model):

    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    texto_comentario = models.TextField()
    def __str__(self):
        return self.texto_comentario