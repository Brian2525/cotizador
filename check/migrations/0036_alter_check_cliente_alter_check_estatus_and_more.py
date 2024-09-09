# Generated by Django 5.1 on 2024-09-04 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0035_alter_check_fecha_expiracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='cliente',
            field=models.ManyToManyField(blank=True, related_name='cliente', to='check.cliente'),
        ),
        migrations.AlterField(
            model_name='check',
            name='estatus',
            field=models.ManyToManyField(blank=True, related_name='status', to='check.status'),
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 4, 18, 12, 39, 143546, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='check',
            name='fecha_solicitud',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='lugar_entrega',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='nombre_empresa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='producto_nuevo',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='volumen_estimado',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]