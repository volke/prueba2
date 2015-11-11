from django.db import models

class mascota (models.Model):
	nombre = models.CharField('Nombre', max_length = 30, null = False)
	raza = models.CharField('Raza', max_length = 30, null = False)
	color = models.CharField('Color', max_length = 30, null = False)
	sexo = models.CharField('Sexo', max_length = 30, null = False)
	descripcion = models.TextField('Descripcion', max_length = 255, blank = True, null = True)
	
	def __unicode__(self):
		return self.nombre
