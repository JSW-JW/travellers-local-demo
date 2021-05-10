from django.urls import path
from diary import views
from django.conf.urls import url


urlpatterns = [
    url('', views.DiaryCreateListAPIView.as_view(), name='diary-list'),
    url('<int:pk>', views.DiaryDetailAPIView.as_view(), name='diary-detail'),
]
