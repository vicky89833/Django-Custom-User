from rest_framework import serializers
from detection_app.models import MediaFile
class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        
        fields = ['id', 'file',  'media_type',]
    
    

class StreamMediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['file', 'output_file', 'media_type', 'uploaded_at', 'user']       
        
class MediaFileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ['id','file', 'output_file']

        