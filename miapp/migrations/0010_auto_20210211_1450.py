# Generated by Django 3.0.5 on 2021-02-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0009_auto_20210211_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otros',
            name='nombre',
        ),
        migrations.AddField(
            model_name='otros',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Miniatura'),
        ),
        migrations.AddField(
            model_name='otros',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='otros',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='otros',
            name='descripcion',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='otros',
            name='lugar',
            field=models.CharField(max_length=100),
        ),
    ]