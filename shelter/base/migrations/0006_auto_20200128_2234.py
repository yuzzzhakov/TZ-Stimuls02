# Generated by Django 3.0.2 on 2020-01-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_dog_fixed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='purpose',
            field=models.ManyToManyField(blank=True, to='base.Dog'),
        ),
    ]
