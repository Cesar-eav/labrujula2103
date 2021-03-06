# Generated by Django 3.0.5 on 2021-02-20 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0017_escaleras_direccion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ascensores',
            options={'ordering': ['-created_at'], 'verbose_name': 'Ascensor', 'verbose_name_plural': 'Ascensores'},
        ),
        migrations.AlterModelOptions(
            name='iglesias',
            options={'ordering': ['-created_at'], 'verbose_name': 'Igleia', 'verbose_name_plural': 'Iglesias'},
        ),
        migrations.AddField(
            model_name='iglesias',
            name='caca',
            field=models.CharField(default='', max_length=100),
        ),
    ]
