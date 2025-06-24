from django.db import models
from django.core.validators import RegexValidator

class Servicio(models.Model):
    titulo = models.CharField("Nombre del Servicio", max_length=100)
    descripcion = models.TextField("Descripción", blank=True, null=True)
    imagen = models.ImageField("Imagen del Servicio", upload_to='servicios/', blank=True, null=True)

    def __str__(self):
        return self.titulo

class SolicitudInformacion(models.Model):
    ESTADOS = [
        ('no_revisada', 'No revisada'),
        ('revisada', 'Revisada'),
    ]

    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(
        max_length=12,
        validators=[
            RegexValidator(
                regex=r'^569\d{8}$',
                message="El teléfono debe tener el formato 569 seguido de 8 números. Ejemplo: 56931931429",
            ),
        ],
        help_text="Ingrese el teléfono en formato 569XXXXXXXX",
    )
    cuando_comenzar = models.CharField(max_length=20)
    requerimientos = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='no_revisada')  # 👈 nuevo campo

    def __str__(self):
        return f"{self.nombre} ({self.email})"

class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, related_name='imagenes_extra', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='servicios/imagenes_extra')

    def __str__(self):
        return f"Imagen de {self.servicio.titulo}"
