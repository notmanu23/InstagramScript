# Generated by Django 4.0.1 on 2022-01-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.IntegerField(default=25),
        ),
    ]