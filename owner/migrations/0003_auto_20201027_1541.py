# Generated by Django 3.1.2 on 2020-10-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_auto_20201023_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=200, unique=True, verbose_name='Slug'),
        ),
    ]
