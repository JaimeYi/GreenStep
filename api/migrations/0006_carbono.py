# Generated by Django 4.2.4 on 2023-11-22 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_profile_image'),
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
                ('reciclaje', models.DecimalField(decimal_places=6, max_digits=7)),
                ('transporte_publico', models.DecimalField(decimal_places=6, max_digits=7)),
                ('jardin', models.DecimalField(decimal_places=6, max_digits=7)),
                ('agua', models.DecimalField(decimal_places=6, max_digits=7)),
            ],
        ),
    ]
