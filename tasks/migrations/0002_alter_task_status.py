# Generated by Django 5.1.6 on 2025-02-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TO_DO', 'Por Hacer'), ('IN_PROGRESS', 'En Progreso'), ('DONE', 'Hecho')], default='todo', max_length=50),
        ),
    ]
