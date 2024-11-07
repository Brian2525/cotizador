# Generated by Django 5.1 on 2024-10-05 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_cliente_empresa_remove_cliente_encargado_cuenta_and_more'),
        ('empresas', '0002_remove_empresa_contactos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa'),
        ),
    ]
