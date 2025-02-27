from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    # Vlores del campo Status
    STATUS = [('TO_DO', 'Por Hacer'), ('IN_PROGRESS', 'En Progreso'), ('DONE', 'Hecho')]

    # Campos tbl_tasks
    task_id = models.AutoField(
        primary_key=True,
        help_text="Identificador único de la tarea."
    )
    title = models.CharField(
        max_length=255,
        help_text="Título de la tarea. Debe ser descriptivo y claro."
    )
    description = models.TextField(
        blank=True, 
        null=True,
        help_text="Descripción detallada de la tarea (opcional)."
    )
    status = models.CharField(
        max_length=50, 
        choices=STATUS, 
        default='TO_DO',
        help_text="Estado actual de la tarea. Valores posibles: TO_DO, IN_PROGRESS, DONE."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Fecha y hora en que la tarea fue creada."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Fecha y hora de la última actualización de la tarea."
    )

    class Meta:
        db_table = 'tbl_tasks'  # Especificar el nombre de la tabla

    def __str__(self):
        return self.title