# Generated by Django 3.1.3 on 2021-03-06 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0021_localthickness'),
    ]

    operations = [
        migrations.AddField(
            model_name='localthickness',
            name='generator_image',
            field=models.TextField(default=''),
        ),
    ]
