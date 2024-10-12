from django.urls import path
from .views import MediaFileUploadView , MediaFileStreamView, UserMediaFileListView
# from user.views import UserRegistrationView
app_name ='detection_app_api'
urlpatterns = [
    path('upload/', MediaFileUploadView.as_view(), name='file-upload'),
    path('mediafile/stream/<int:pk>/', MediaFileStreamView.as_view(), name='mediafile-stream'),
    path('user/mediafiles/', UserMediaFileListView.as_view(), name='user-mediafile-list'),
    # path('register/', UserRegistrationView.as_view(), name='user-registration'),
]
