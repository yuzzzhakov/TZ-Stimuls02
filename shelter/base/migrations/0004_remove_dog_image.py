# Generated by Django 3.0.2 on 2020-01-26 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20200124_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='image',
        ),
    ]
