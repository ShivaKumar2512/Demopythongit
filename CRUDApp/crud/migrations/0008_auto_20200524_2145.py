# Generated by Django 3.0.5 on 2020-05-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_auto_20200524_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='crud.Tag'),
        ),
    ]
