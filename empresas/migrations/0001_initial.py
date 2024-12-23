# Generated by Django 5.1 on 2024-10-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0002_delete_empresa_cliente_posicion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('contactos', models.ManyToManyField(related_name='trabajadores', to='clientes.cliente')),
            ],
        ),
    ]
