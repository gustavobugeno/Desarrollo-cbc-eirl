import random
import string
from django.db import models
from django.core.validators import RegexValidator

# ⭐ IMPORTS PARA CLOUDINARY
from cloudinary_storage.storage import (
    MediaCloudinaryStorage,
    RawMediaCloudinaryStorage
)

# --------------------------------------------
#   Generador de CÓDIGO DE SEGUIMIENTO
# --------------------------------------------
def generar_codigo():
    año = "2025"
    numero = ''.join(random.choices(string.digits, k=5))
    return f"CBC-{año}-{numero}"


# --------------------------------------------
#   MODELO SERVICIO
# --------------------------------------------
class Servicio(models.Model):
    titulo = models.CharField("Nombre del Servicio", max_length=100)
    descripcion = models.TextField("Descripción", blank=True, null=True)

    imagen = models.ImageField(
        "Imagen del Servicio",
        upload_to='servicios/',
        storage=MediaCloudinaryStorage(),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo


# --------------------------------------------
#   MODELO SOLICITUD DE INFORMACIÓN
# --------------------------------------------
class SolicitudInformacion(models.Model):

    ESTADOS = [
        ('no_revisada', 'No revisada'),
        ('revisada', 'Revisada por experto'),
        ('asignada', 'Experto asignado'),
        ('cotizada', 'Cotización generada'),
        ('enviada', 'Cotización enviada'),
        ('aceptada', 'Aceptada'),
        ('rechazada', 'Rechazada'),
        ('pagada', 'Pagada'),
    ]

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        related_name="solicitudes",
        null=True,
        blank=True,
    )

    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    telefono = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^569\d{8}$',
                message="El teléfono debe tener el formato 569XXXXXXXX",
            ),
        ],
    )

    tienes_terreno = models.CharField(
        max_length=10,
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )

    ubicacion = models.CharField(max_length=255)
    cuando_comenzar = models.CharField(max_length=20)
    requerimientos = models.TextField()

    estado = models.CharField(max_length=20, choices=ESTADOS, default='no_revisada')
    fecha_envio = models.DateTimeField(auto_now_add=True)

    codigo_seguimiento = models.CharField(max_length=30, unique=True, blank=True)

    comentarios_cambios = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.codigo_seguimiento:
            self.codigo_seguimiento = generar_codigo()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.codigo_seguimiento}"


# --------------------------------------------
#   MODELO IMÁGENES EXTRA
# --------------------------------------------
class ImagenServicio(models.Model):
    servicio = models.ForeignKey(
        Servicio,
        related_name='imagenes_extra',
        on_delete=models.CASCADE
    )

    imagen = models.ImageField(
        upload_to='servicios/imagenes_extra/',
        storage=MediaCloudinaryStorage()
    )

    def __str__(self):
        return f"Imagen de {self.servicio.titulo}"


# --------------------------------------------
#   MODELO PRESUPUESTO (PDF — RAW)
# --------------------------------------------
class Presupuesto(models.Model):
    solicitud = models.OneToOneField(
        'SolicitudInformacion',
        on_delete=models.CASCADE,
        related_name='presupuesto'
    )

    archivo = models.FileField(
        upload_to='presupuestos/',
        storage=RawMediaCloudinaryStorage()
    )

    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Presupuesto de {self.solicitud.codigo_seguimiento}"
