# Generated by Django 5.1 on 2024-09-06 06:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0005_alter_check_fecha_expiracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('aprobado', 'aprobado'), ('rechazado', 'rechazado')], default='pendiente', max_length=10),
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 6, 5, 45, 993560, tzinfo=datetime.timezone.utc)),
        ),
    ]
