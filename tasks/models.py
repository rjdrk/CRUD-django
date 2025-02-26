from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    STATUS = [('TO_DO', 'Por Hacer'), ('IN_PROGRESS', 'En Progreso'), ('DONE', 'Hecho')]

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default='TO_DO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_tasks'  # Especificar el schema

    def __str__(self):
        return self.title