from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from posts.models import Noticia, Comentario
from django.shortcuts import render, get_object_or_404
from agenda.models import Agenda
from django.urls import reverse
from gallery.models import Imagen
from django.utils import timezone
from django.views import generic

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class NoticiaListView(generic.ListView):
    model = Noticia
    template_name = 'noticia.html'

class MultimediaView(TemplateView):
    template_name = 'multimedia.html'

class AgendaListView(generic.ListView):
    model = Agenda
    template_name = 'agenda.html'

class AgendaDetailView(generic.DetailView):
    model = Agenda
    template_name = 'agenda_detail.html'
    slug_field = 'titulo_agenda'

class ServiciosView(TemplateView):
    template_name = 'servicios.html'

class CentrosView(TemplateView):
    template_name = 'centros.html'

class ImagenListView(generic.ListView):
    model = Imagen
    template_name = 'galeria.html'
