# Generated by Django 3.2.4 on 2021-06-23 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantite',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]