# Generated by Django 5.1 on 2024-09-02 20:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0034_alter_check_fecha_expiracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='fecha_expiracion',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 2, 20, 19, 44, 55899, tzinfo=datetime.timezone.utc)),
        ),
    ]
