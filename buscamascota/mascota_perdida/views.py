from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from .models import mascota_perdida

class mascota_perdida_view(ListView):
	model = mascota_perdida
	fields = '__all__'
	template_name = 'mascota_perdida/lista_mascota_perdida.html'
listar_mascota_perdida = mascota_perdida_view.as_view()

class mascota_encontrada_view(ListView):
	model = mascota_perdida
	fields = '__all__'
	template_name = 'mascota_perdida/lista_mascota_encontrada.html'
listar_mascota_encontrada = mascota_encontrada_view.as_view()

class mascota_perdida_update(UpdateView):
	model = mascota_perdida
	template_name = 'mascota_perdida/update.html'
	fields = '__all__'
update_mascota_perdida = mascota_perdida_update.as_view()	

class mascota_perdida_delete(DeleteView):
    model = mascota_perdida
    template_name = "mascota_perdida/mascota_perdida_confirm_delete.html"
delete_mascota_perdida =mascota_perdida_delete.as_view()