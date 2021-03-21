# Generated by Django 3.0.5 on 2021-02-10 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0005_auto_20210210_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miradores',
            name='description',
        ),
        migrations.RemoveField(
            model_name='miradores',
            name='name',
        ),
        migrations.AddField(
            model_name='miradores',
            name='calle',
            field=models.CharField(default='calle', max_length=100, verbose_name='calle'),
        ),
        migrations.AddField(
            model_name='miradores',
            name='gps',
            field=models.CharField(default='gps', max_length=100, verbose_name='GPS'),
        ),
        migrations.AddField(
            model_name='miradores',
            name='image',
            field=models.ImageField(default='null', upload_to='articles', verbose_name='Miniatura'),
        ),
        migrations.AddField(
            model_name='miradores',
            name='lugar',
            field=models.CharField(default='cerro', max_length=100, verbose_name='Lugar'),
        ),
        migrations.AddField(
            model_name='miradores',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='miradores',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]