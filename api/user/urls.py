from django.urls import path, re_path

from user.views import register_user, get_dynamics, add_dynamic, get_comments, add_comment, finish_test, get_gone, \
    get_achievement, upload_image, dynamic_like

USER_URL = [
    path('api/register_user/', register_user, name='register_user'),
    path('api/get_dynamics/', get_dynamics, name='get_dynamics'),
    path('api/add_dynamic/', add_dynamic, name='add_dynamic'),
    path('api/upload_image/', upload_image, name='upload_image'),
    path('api/get_comments/', get_comments, name='get_comments'),
    path('api/add_comment', add_comment, name='add_comment'),
    path('api/finish_test', finish_test, name='finish_test'),
    path('api/get_gone', get_gone, name='get_gone'),
    path('api/get_achievement', get_achievement, name='get_achievement'),
    path('api/dynamic_like', dynamic_like, name='dynamic_like')
]
