# Generated by Django 3.0.5 on 2021-03-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0026_auto_20210315_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ascensores',
            name='image',
            field=models.ImageField(default='null', upload_to='ascensores', verbose_name='Miniatura'),
        ),
        migrations.AlterField(
            model_name='escaleras',
            name='image',
            field=models.ImageField(default='null', upload_to='escaleras', verbose_name='Miniatura'),
        ),
    ]
