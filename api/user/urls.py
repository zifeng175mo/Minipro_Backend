from django.urls import path, re_path

from user.views import register_user

USER_URL = [
    path('api/register_user/', register_user, name='register_user'),
]
