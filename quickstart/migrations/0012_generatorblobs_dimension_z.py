# Generated by Django 3.1.3 on 2021-01-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0011_auto_20210111_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatorblobs',
            name='dimension_z',
            field=models.IntegerField(blank=True, default=500, null=True),
        ),
    ]
