from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from posts.models import Noticia
from . import views
from .views import AgendaDetailView, HomePageView, AboutView, NoticiaListView, ImagenListView, MultimediaView, AgendaListView, ServiciosView, CentrosView
app_name = 'agenda'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('noticia/', NoticiaListView.as_view(), name='noticia'),
    path('multimedia/', MultimediaView.as_view(), name='multimedia'),
    path('agenda/', AgendaListView.as_view(), name='agenda'),
    path('agenda/<str:pk>/', AgendaDetailView.as_view(), name='agenda_detail'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('centros/', CentrosView.as_view(), name='centros'),
    path('galeria/', ImagenListView.as_view(), name='imagen'),
    
]