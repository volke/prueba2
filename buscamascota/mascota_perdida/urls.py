from django.conf.urls import url
from .import views

urlpatterns= [

	url(r'^listar_perdidas/$', views.listar_mascota_perdida, name='listar_perdidas'),
	url(r'^listar_encontradas/$', views.listar_mascota_encontrada, name='listar_encontradas'),
	url(r'^actualizar/(?P<pk>\d+)/$', views.update_mascota_perdida, name='actualizar'),
	url(r'^eliminar/(?P<pk>\d+)/$', views.delete_mascota_perdida, name='eliminar'),
	]