from django.urls import path, re_path

from province.views import get_poem

PROVINCE_URL = [
    path('api/get_poem/', get_poem, name='get_poem'),
]
