from django.db import models


class Deal(models.Model):
    STATUS_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('en_progreso', 'En Progreso'),
        ('ganado', 'Ganado'),
        ('perdido', 'Perdido'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nuevo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.title