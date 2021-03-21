# Generated by Django 3.0.5 on 2021-02-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0018_auto_20210220_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iglesias',
            old_name='caca',
            new_name='direccion',
        ),
        migrations.RemoveField(
            model_name='iglesias',
            name='lugar',
        ),
        migrations.AddField(
            model_name='iglesias',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
    ]
