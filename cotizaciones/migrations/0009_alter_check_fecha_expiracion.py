# Generated by Django 5.1 on 2024-09-06 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0008_alter_check_comentarios_adicionales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 6, 20, 26, 55, 64222, tzinfo=datetime.timezone.utc)),
        ),
    ]