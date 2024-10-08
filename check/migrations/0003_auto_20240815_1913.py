# Generated by Django 3.2.23 on 2024-08-16 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_check_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='check',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='check',
            name='precio',
        ),
        migrations.AddField(
            model_name='check',
            name='comentarios_adicionales',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='fecha_solicitud',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='frecuencia_compra',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='lugar_entrega',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='nombre_cliente',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='nombre_gerente',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='nombre_proyecto',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='numero_tintas',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='precio_objetivo',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='producto_nuevo',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='tecnologia_fabricacion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='tipo_producto',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='volumen_estimado',
            field=models.IntegerField(null=True),
        ),
    ]
