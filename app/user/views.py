from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from user import serializers
from user import models
from user import permissions

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.shortcuts import render

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.views.generic.base import TemplateView, View
from django.middleware.csrf import _compare_masked_tokens

from user.oauth.providers.naver import NaverLoginMixin


def login(request):
    return render(request, 'user/login_form.html')


class SocialLoginCallbackView(NaverLoginMixin, View):

    success_url = settings.LOGIN_REDIRECT_URL
    failure_url = settings.LOGIN_URL
    required_profiles = ['email', 'name']
    model = get_user_model()

    def get(self, request, *args, **kwargs):

        provider = kwargs.get('provider')

        if provider == 'naver': # 프로바이더가 naver 일 경우
            csrf_token = request.GET.get('state')
            code = request.GET.get('code')
            if not _compare_masked_tokens(csrf_token, request.COOKIES.get('csrftoken')): # state(csrf_token)이 잘못된 경우
                messages.error(request, '잘못된 경로로 로그인하셨습니다.', extra_tags='danger')
                print("Not match")
                return redirect(self.failure_url)
            is_success, error = self.login_with_naver(csrf_token, code)
            if not is_success: # 로그인 실패할 경우
                messages.error(request, error, extra_tags='danger')
            return redirect(self.success_url if is_success else self.failure_url)

        return redirect(self.failure_url)

    def set_session(self, **kwargs):
        for key, value in kwargs.items():
            self.request.session[key] = value


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES # enable ObtainAuthToken class in the Django admin
