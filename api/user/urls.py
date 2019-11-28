from django.urls import path, re_path

from user.views import register_user, get_dynamics, add_dynamic

USER_URL = [
    path('api/register_user/', register_user, name='register_user'),
    path('api/get_dynamics/', get_dynamics, name='get_dynamics'),
    path('api/add_dynamic/', add_dynamic, name='add_dynamic'),
]
