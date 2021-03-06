# Generated by Django 3.0.3 on 2020-03-25 20:54

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(upload_to=music.models.image_directory_path),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to=music.models.image_directory_path),
        ),
    ]
