from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import mascota

class mascota_view(ListView):
	model = mascota
	template_name = 'mascota/listar.html'
listar_mascota = mascota_view.as_view()

class mascota_create(CreateView):
	model = mascota
	template_name = 'mascota/crear.html'
	fields = '__all__'
	success_url = reverse_lazy ('listar')
crear_mascota = mascota_create.as_view()