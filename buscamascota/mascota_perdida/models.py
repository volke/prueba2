from django.db import models

class mascota_perdida(models.Model):

	nombre = models.CharField('Nombre', max_length=50)
	tipo = models.CharField('Tipo', max_length=50)
	raza = models.CharField('Raza', max_length=50)
	color = models.CharField('Color', max_length=50)
	sexo = models.CharField('Sexo', max_length=50)
	sector = models.CharField('Sector', max_length=50)
	direccion = models.CharField('Direccion', max_length=50)
	datos_adicionales = models.TextField('Datos adicionales', max_length=500)
	foto = models.FileField('Foto', blank = True)
	perdido = models.BooleanField('Esta perdido?')
	
	def __unicode__(self):
		return self.nombre
    
