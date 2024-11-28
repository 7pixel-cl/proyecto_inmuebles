# Generated by Django 5.1.3 on 2024-11-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0009_inmueble_image_filename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inmueble',
            name='image_filename',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='inmuebles/'),
        ),
    ]
