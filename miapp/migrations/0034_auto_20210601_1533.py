# Generated by Django 3.0.5 on 2021-06-01 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0033_auto_20210601_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mira',
            old_name='long',
            new_name='lon',
        ),
    ]