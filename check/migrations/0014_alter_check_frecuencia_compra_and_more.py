# Generated by Django 5.1 on 2024-08-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0013_alter_check_motivo_rechazo_delete_reject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='frecuencia_compra',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='motivo_rechazo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]