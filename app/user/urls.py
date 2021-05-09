from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
    path('login/social/<provider>/callback/', views.SocialLoginCallbackView.as_view()),
    url('login/', views.login, name='login'),
]
