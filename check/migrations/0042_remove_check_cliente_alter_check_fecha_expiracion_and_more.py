# Generated by Django 5.1 on 2024-09-05 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0041_remove_check_cliente_alter_check_fecha_expiracion_and_more'),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='cliente',
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 5, 18, 32, 34, 286901, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='check',
            name='cliente',
            field=models.ManyToManyField(blank=True, max_length=100, to='clientes.cliente'),
        ),
    ]
