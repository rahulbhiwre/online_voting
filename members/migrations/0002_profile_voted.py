# Generated by Django 3.0.3 on 2020-07-03 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='voted',
            field=models.BooleanField(default=False),
        ),
    ]
