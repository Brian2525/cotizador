# Generated by Django 5.1 on 2024-09-05 22:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0004_alter_check_cliente_alter_check_fecha_expiracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 5, 22, 5, 24, 478995, tzinfo=datetime.timezone.utc)),
        ),
    ]
