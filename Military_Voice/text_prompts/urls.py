from django.urls import path
from .views import sentence_list, sentence_detail, sentence_upload

urlpatterns = [
    path('sentences/', sentence_list),
    path('detail/<int:pk>/', sentence_detail),
    path('upload-csv/', sentence_upload, name="sentence_upload")
]
