from django.contrib import admin
from django.utils.html import format_html
from .models import Servicio, ImagenServicio, SolicitudInformacion, Presupuesto

# ----------------------------
#  ADMIN PARA PRESUPUESTOS
# ----------------------------
class PresupuestoInline(admin.StackedInline):
    model = Presupuesto
    extra = 0
    max_num = 1

@admin.register(Presupuesto)
class PresupuestoAdmin(admin.ModelAdmin):
    list_display = ('solicitud', 'fecha', 'total')


# ----------------------------
#  ADMIN PARA SOLICITUDES CON SEGUIMIENTO
# ----------------------------
@admin.register(SolicitudInformacion)
class SolicitudInformacionAdmin(admin.ModelAdmin):
    inlines = [PresupuestoInline]

    # Mostrar estado con colores
    def estado_coloreado(self, obj):
        colores = {
            'no_revisada': 'orange',
            'revisada': 'blue',
            'asignada': 'purple',
            'cotizada': 'darkblue',
            'enviada': 'teal',
            'aceptada': 'green',
            'rechazada': 'red',
            'pagada': 'darkgreen',
        }
        color = colores.get(obj.estado, 'black')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_estado_display()
        )
    estado_coloreado.short_description = "Estado"

    # Campos que se muestran en el admin
    list_display = (
        'codigo_seguimiento',
        'nombre',
        'email',
        'telefono',
        'servicio',
        'estado_coloreado',
        'fecha_envio'
    )

    search_fields = ('nombre', 'email', 'telefono', 'codigo_seguimiento')
    list_filter = ('estado', 'servicio', 'fecha_envio')
    ordering = ('-fecha_envio',)


# ----------------------------
#  ADMIN PARA SERVICIOS
# ----------------------------
class ImagenServicioInline(admin.TabularInline):
    model = ImagenServicio
    extra = 1

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    inlines = [ImagenServicioInline]
