"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from project import settings
from province.urls import PROVINCE_URL
from user.urls import USER_URL
from ws.routing import WEBSOCKET_URL

urlpatterns = [
                  path('admin/', admin.site.urls, name='admin'),
                  re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  re_path(r'^static/(?P<path>.*)$', serve,
                          {'document_root': settings.STATIC_ROOT}),
              ] + PROVINCE_URL + USER_URL + WEBSOCKET_URL
