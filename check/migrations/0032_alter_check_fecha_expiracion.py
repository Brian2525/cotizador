# Generated by Django 5.1 on 2024-09-02 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0031_alter_check_fecha_expiracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 19, 55, 47, 861390, tzinfo=datetime.timezone.utc)),
        ),
    ]