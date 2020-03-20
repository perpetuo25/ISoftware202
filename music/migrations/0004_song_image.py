# Generated by Django 3.0.3 on 2020-03-20 02:18

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20200319_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='music/media/images/noim.png', upload_to=music.models.image_directory_path),
        ),
    ]