# Generated by Django 4.2.4 on 2023-11-22 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_carbono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbono',
            old_name='reciclaje',
            new_name='reciclaje_c',
        ),
    ]