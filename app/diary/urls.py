from django.urls import path
from diary import views
from django.conf.urls import url


urlpatterns = [
    url(r'^diary_list$', views.diary_list, name='diary_list'),
    url(r'^(?P<pk>\d+)/$', views.diary_detail, name='diary_detail'),
]
