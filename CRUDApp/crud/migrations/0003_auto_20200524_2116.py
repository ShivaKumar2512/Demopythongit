# Generated by Django 3.0.5 on 2020-05-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_auto_20200524_2115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='price',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='description',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door')], max_length=200, null=True),
        ),
    ]
