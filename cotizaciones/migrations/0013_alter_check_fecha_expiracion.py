# Generated by Django 5.1 on 2024-09-11 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotizaciones', '0012_alter_check_fecha_expiracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 21, 21, 32, 6, 136705, tzinfo=datetime.timezone.utc)),
        ),
    ]
