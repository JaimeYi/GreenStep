# Generated by Django 4.2.4 on 2023-11-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GreenStepApp', '0005_encuesta_suma_puntaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoEncuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato_encuesta', models.IntegerField()),
                ('fecha_encuesta', models.IntegerField()),
            ],
        ),
    ]
