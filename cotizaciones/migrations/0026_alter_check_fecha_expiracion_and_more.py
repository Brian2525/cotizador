# Generated by Django 5.1 on 2024-10-03 21:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0025_alter_check_fecha_expiracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 13, 21, 55, 17, 5712, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_solicitud',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 15, 55, 17, 5712)),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 3, 15, 55, 17, 7712)),
        ),
    ]