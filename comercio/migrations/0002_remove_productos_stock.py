# Generated by Django 4.0.6 on 2022-08-07 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='stock',
        ),
    ]
