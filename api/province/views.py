import json

import django
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse

from province.models import Province, Test, Poem


# Create your views here.

def get_poem(request):
    province = request.GET.get('province')
    if not province:
        return JsonResponse({'status': False, 'error': '省份不存在'})
    province = Province.objects.filter(name=province)
    province = province[0]
    poems = Poem.objects.filter(province=province)
    return_poems = []
    for poem in poems:
        return_poems.append({
            'poem_name': poem.poem_name,
            'poem_content': poem.poem_content,
            'author': poem.author,
            'translation': poem.translation,
            'introduction': poem.introduction
            })
    return JsonResponse(
        {'status': True, 'data': return_poems, 'province': province.name_ch})


def get_test(request):
    province = request.GET.get('province')
    if not province:
        return JsonResponse({'status': False, 'error': '省份不存在'})
    province = Province.objects.filter(name=province)
    province = province[0]
    test_list = []
    test = Test.objects.filter(province=province)
    if not test:
        return JsonResponse({'status': False, 'error': '未查到相关题库'})
    else:
        for index in test:
            test_list.append({
                'question': index.question,
                'options': [
                    index.option_A, index.option_B, index.option_C, index.option_D
                ],
                'answer': index.answer
            })
    return JsonResponse({'status': True, 'data': test_list})
