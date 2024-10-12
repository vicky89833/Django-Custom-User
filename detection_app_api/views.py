
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from detection_app.models import MediaFile
from .serializers import MediaFileSerializer, StreamMediaFileSerializer, MediaFileListSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import FileResponse, Http404

class MediaFileUploadView(mixins.CreateModelMixin, generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    parser_classes = [MultiPartParser, FormParser]  # To handle file uploads

    def post(self, request, *args, **kwargs):
        # Handle file upload
        print(request.data)
        return self.create(request, *args, **kwargs)
    def perform_create(self, serializer):
        # Automatically set the current user when saving the MediaFile instance
        serializer.save(user=self.request.user)
        

class MediaFileStreamView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, *args, **kwargs):
        try:
            media_file = MediaFile.objects.get(pk=pk)
            if media_file.output_file:
                response = StreamMediaFileSerializer(media_file.output_file.open(), content_type='video/mp4')
                response['Content-Disposition'] = f'inline; filename={media_file.output_file.name}'
                return response
            else:
                return Http404("Output file not available.")
        except MediaFile.DoesNotExist:
            raise Http404("Media file not found.")

class UserMediaFileListView(generics.ListAPIView):
    serializer_class = MediaFileListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MediaFile.objects.filter(user=self.request.user)        