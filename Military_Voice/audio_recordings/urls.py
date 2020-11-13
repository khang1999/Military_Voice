from django.urls import path
from .views import recordings_list, recordings_detail, recordings_download, recordings_audio_download
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recordings/', recordings_list),
    path('recording_detail/<int:pk>/', recordings_detail),
    path('download-csv/', recordings_download),
    path('download-audio/', recordings_audio_download)
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)