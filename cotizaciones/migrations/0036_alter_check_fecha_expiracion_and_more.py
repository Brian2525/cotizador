# Generated by Django 5.1 on 2024-10-05 19:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0035_alter_check_fecha_expiracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 15, 19, 45, 25, 154544, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_solicitud',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 13, 45, 25, 154544)),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 13, 45, 25, 155544)),
        ),
    ]