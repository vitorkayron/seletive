# Generated by Django 4.1.3 on 2022-11-12 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_rename_tecnologias_tecnologia'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='tecnologias',
            new_name='tecnologia',
        ),
    ]
