# Generated by Django 3.0.5 on 2020-04-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectors', '0008_auto_20200419_1106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lector',
            name='lectorn/',
        ),
        migrations.AddField(
            model_name='lector',
            name='image',
            field=models.ImageField(default='null', upload_to='', verbose_name='Изображение'),
        ),
    ]