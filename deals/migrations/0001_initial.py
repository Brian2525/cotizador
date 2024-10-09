# Generated by Django 5.1 on 2024-10-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('nuevo', 'Nuevo'), ('en_progreso', 'En Progreso'), ('ganado', 'Ganado'), ('perdido', 'Perdido')], default='nuevo', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.CharField(max_length=200)),
            ],
        ),
    ]