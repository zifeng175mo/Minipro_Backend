from django.urls import path, re_path

from province.views import get_poem, get_test

PROVINCE_URL = [
    path('api/get_poem/', get_poem, name='get_poem'),
    path('api/get_test/', get_test, name='get_test'),
]
