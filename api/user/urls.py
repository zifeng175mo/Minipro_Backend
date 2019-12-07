from django.urls import path, re_path

from user.views import register_user, get_dynamics, add_dynamic, get_comments, add_comment

USER_URL = [
    path('api/register_user/', register_user, name='register_user'),
    path('api/get_dynamics/', get_dynamics, name='get_dynamics'),
    path('api/add_dynamic/', add_dynamic, name='add_dynamic'),
    path('api/get_comments/', get_comments, name='get_comments'),
    path('api/add_comment', add_comment, name='add_comment')
]
