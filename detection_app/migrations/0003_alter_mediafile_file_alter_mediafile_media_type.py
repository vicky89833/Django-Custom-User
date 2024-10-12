# Generated by Django 5.1.2 on 2024-10-10 19:02

import detection_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection_app', '0002_mediafile_output_file_mediafile_user_imagelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediafile',
            name='file',
            field=models.FileField(upload_to='uploads/', validators=[detection_app.models.validate_video_file]),
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='media_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video')], default='video', max_length=10),
        ),
    ]
