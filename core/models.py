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
        on_delete=models.CA_

