# Generated by Django 3.2.4 on 2021-06-21 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='nom',
            new_name='nom_categorie',
        ),
        migrations.RenameField(
            model_name='marque',
            old_name='nom',
            new_name='nom_marque',
        ),
    ]
