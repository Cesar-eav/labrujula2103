# Generated by Django 3.0.5 on 2021-06-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0035_arquitectura'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquitectura',
            name='publicidad',
            field=models.BooleanField(default=False, verbose_name='Publicidad'),
        ),
    ]