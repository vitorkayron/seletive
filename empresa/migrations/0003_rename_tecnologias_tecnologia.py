# Generated by Django 4.1.3 on 2022-11-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_empresa'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tecnologias',
            new_name='Tecnologia',
        ),
    ]