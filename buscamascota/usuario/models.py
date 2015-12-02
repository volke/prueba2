from django.db import models
from django.contrib.auth.models import User

class usuario(User):
	direccion = models.CharField('direccion', max_length = 50, blank = True)
	telefono = models.IntegerField('telefono', blank = True)
	caza_recompenza = models.BooleanField('caza_recompenza')

	def __unicode__(self):
		return self.user.username