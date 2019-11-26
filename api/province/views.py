import json

import django
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpRequest, JsonResponse

from province.models import Province


# Create your views here.

def get_poem(request):
    province = request.GET.get('province')
    if not province:
        return JsonResponse({'status': False, 'error': '省份不存在'})
    print(province)
    poem_name = Province.objects.all()[0].poem_name
    poem_content = Province.objects.all()[0].poem_content
    author = Province.objects.all()[0].author
    translation = Province.objects.all()[0].translation
    return JsonResponse({'status': True, 'poem_name': poem_name, 'poem_content': poem_content, 'author': author,
                         'translation': translation})
