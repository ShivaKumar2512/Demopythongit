# Generated by Django 3.0.5 on 2020-05-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_auto_20200524_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custome',
            new_name='customer',
        ),
    ]
