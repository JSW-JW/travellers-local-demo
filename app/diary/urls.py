from django.urls import path
from diary import views
from django.conf.urls import url


urlpatterns = [
    path('', views.DiaryCreateListAPIView.as_view(), name='diary-list'),
    path('<int:pk>/', views.DiaryDetailAPIView.as_view(), name='diary-detail'),
    path('<int:pk>/upload-image/', views.ImageCreateListAPIView.as_view(), name='upload-image')
]
