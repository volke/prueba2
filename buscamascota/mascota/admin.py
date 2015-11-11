from django.contrib import admin
from .models import mascota
# Register your models here.
@admin.register(mascota)
class MascotaAdmin(admin.ModelAdmin):
    pass