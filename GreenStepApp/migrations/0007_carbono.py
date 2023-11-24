# Generated by Django 4.2.4 on 2023-11-22 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GreenStepApp', '0006_encuesta_carbono_generado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carbono',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbono_auto', models.DecimalField(decimal_places=6, max_digits=7)),
                ('carbono_electricidad', models.DecimalField(decimal_places=6, max_digits=7)),
                ('carbono_vuelos', models.DecimalField(decimal_places=6, max_digits=7)),
                ('carne', models.DecimalField(decimal_places=6, max_digits=7)),
                ('reciclaje_c', models.DecimalField(decimal_places=6, max_digits=7)),
                ('transporte_publico', models.DecimalField(decimal_places=6, max_digits=7)),
                ('jardin_c', models.DecimalField(decimal_places=6, max_digits=7)),
                ('agua', models.DecimalField(decimal_places=6, max_digits=7)),
                ('fecha_respuesta', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]