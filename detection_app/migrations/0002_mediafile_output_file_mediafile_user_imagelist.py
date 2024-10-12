# Generated by Django 5.1.2 on 2024-10-10 18:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='output_file',
            field=models.FileField(blank=True, null=True, upload_to='outputs/'),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='media_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ImageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('images', models.ManyToManyField(related_name='image_lists', to='detection_app.mediafile')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='image_lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
