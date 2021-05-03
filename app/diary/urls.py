from django.urls import path
from diary import views
from django.conf.urls import url


urlpatterns = [
    url('', views.DiaryView.as_view(), name='DiaryView'),
    url(r'^(?P<pk>\d+)/$', views.diary_detail, name='diary_detail'),
]
