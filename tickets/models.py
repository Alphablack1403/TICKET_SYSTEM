from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):

    class Estado(models.TextChoices):
        ABIERTO = 'ABIERTO', 'Abierto'
        EN_PROGRESO = 'EN_PROGRESO', 'En progreso'
        CERRADO = 'CERRADO', 'Cerrado'

    class Prioridad(models.TextChoices):
        BAJA = 'BAJA', 'Baja'
        MEDIA = 'MEDIA', 'Media'
        ALTA = 'ALTA', 'Alta'

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    prioridad = models.CharField(
        max_length=10,
        choices=Prioridad.choices,
        default=Prioridad.MEDIA
    )
    estado = models.CharField(
        max_length=20,  
        choices=Estado.choices,
        default=Estado.ABIERTO
    )
    
    usuario = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='tickets',
    null=True,
    blank=True
    )

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - {self.estado}"


class Comentario(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comentarios'
    )
    descripcion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['fecha_registro']

    def __str__(self):
        return f"{self.usuario.username} - {self.ticket.titulo}"

