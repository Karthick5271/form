from django.urls import path
from . import views

urlpatterns = [
    path('', views.FileUploadView.as_view(), name='upload'),
    path('list/', views.FileListView.as_view(), name='list'),
    path('get-photos/<str:folder_id>/', views.GetPhotosView.as_view(), name='get_photos'),
]
