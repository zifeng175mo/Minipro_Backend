import json

import django
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse

from province.models import Province


# Create your views here.

def get_poem(request):
    province = request.GET.get('province')
    if not province:
        return JsonResponse({'status': False, 'error': '省份不存在'})
    province = Province.objects.filter(name=province)
    province = province[0]
    name_ch = province.name_ch
    poem_name = province.poem_name
    poem_content = province.poem_content
    author = province.author
    translation = province.translation
    introduction = province.introduction
    return JsonResponse(
        {'status': True, 'name': name_ch, 'poem_name': poem_name, 'poem_content': poem_content, 'author': author,
         'translation': translation, 'introduction': introduction})
