# Generated by Django 4.2.4 on 2023-11-22 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_reciclaje_carbono_reciclaje_c'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbono',
            old_name='jardin',
            new_name='jardin_c',
        ),
    ]