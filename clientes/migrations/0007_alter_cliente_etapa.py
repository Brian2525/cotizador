# Generated by Django 5.1 on 2024-10-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_alter_cliente_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='etapa',
            field=models.CharField(choices=[('inicial', 'Inicial'), ('primer_contacto', 'Primer Contacto'), ('seguimiento', 'Seguimiento'), ('propuesta_enviada', 'Propuesta Enviada'), ('cerrado', 'Cerrado'), ('perdido', 'Perdido'), ('es_cliente', 'Es cliente')], default='inicial', max_length=50),
        ),
    ]
