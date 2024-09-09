# Generated by Django 5.1 on 2024-09-05 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0039_alter_check_autor_remove_check_cliente_and_more'),
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
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 5, 18, 14, 12, 906960, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AddField(
            model_name='check',
            name='cliente',
            field=models.ManyToManyField(blank=True, related_name='cliente', to='clientes.cliente'),
        ),
    ]