# Generated by Django 5.1 on 2024-10-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_remove_producto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('producto', 'Producto'), ('servicio', 'Servicio')], max_length=10, null=True),
        ),
    ]