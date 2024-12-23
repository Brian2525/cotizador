# Generated by Django 5.1 on 2024-10-05 21:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_etapa'),
        ('deals', '0001_initial'),
        ('empresas', '0002_remove_empresa_contactos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente'),
        ),
        migrations.AddField(
            model_name='deal',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa'),
        ),
        migrations.RemoveField(
            model_name='deal',
            name='owner',
        ),
        migrations.AddField(
            model_name='deal',
            name='owner',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
