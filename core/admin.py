from django.contrib import admin
from .models import Servicio, ImagenServicio, SolicitudInformacion

class ImagenServicioInline(admin.TabularInline):
    model = ImagenServicio
    extra = 1

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    inlines = [ImagenServicioInline]

@admin.register(SolicitudInformacion)
class SolicitudInformacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'estado')
    list_filter = ('estado',)
    search_fields = ('nombre', 'email', 'telefono')
