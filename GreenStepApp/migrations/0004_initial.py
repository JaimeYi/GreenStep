# Generated by Django 4.2.4 on 2023-11-12 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GreenStepApp', '0003_remove_task_project_delete_project_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kms_conducidos', models.IntegerField()),
                ('promedio_electricidad', models.IntegerField()),
                ('vuelos', models.IntegerField()),
                ('carnes_rojas', models.IntegerField()),
                ('reciclaje', models.IntegerField()),
                ('transporte', models.IntegerField()),
                ('jardin', models.IntegerField()),
                ('agua_promedio', models.IntegerField()),
                ('fecha_respuesta', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
