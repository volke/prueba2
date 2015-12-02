from django.contrib import admin
from .models import mascota_perdida

@admin.register(mascota_perdida)
class MascotaPerdidaAdmin(admin.ModelAdmin):
    pass

# Register your models here.
