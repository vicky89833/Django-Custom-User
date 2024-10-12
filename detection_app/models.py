 

from django.db import models
from user.models import NewUser

from django.core.exceptions import ValidationError
import mimetypes




def validate_video_file(value):
    # Check the file's MIME type to ensure it's a video
    valid_video_mimetypes = ['video/mp4', 'video/avi', 'video/mpeg', 'video/quicktime']
    file_mimetype = mimetypes.guess_type(value.name)[0]
    
    if file_mimetype not in valid_video_mimetypes:
        raise ValidationError('Unsupported file type. Please upload a valid video file.')


class MediaFile(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    file = models.FileField(upload_to='uploads/', validators=[validate_video_file])
    output_file = models.FileField(upload_to='outputs/', blank=True, null=True)  # New output_file field
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES, default='video')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='media_files', default=1)

    def __str__(self):
        return f"{self.media_type}: {self.file.name}"

class ImageList(models.Model):
    title = models.CharField(max_length=255)  # Optional title for the image list
    images = models.ManyToManyField(MediaFile, related_name='image_lists')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='image_lists', default=1)

    def __str__(self):
        return self.title