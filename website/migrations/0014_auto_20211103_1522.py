# Generated by Django 3.2.4 on 2021-11-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_alter_orderitem_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='prix',
            field=models.IntegerField(max_length=50),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='prix',
            field=models.IntegerField(),
        ),
    ]