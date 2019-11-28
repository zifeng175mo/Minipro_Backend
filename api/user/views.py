from django.shortcuts import render
import django
import json
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
from user.util import get_page

from user.models import User, Dynamics, DynamicsPicture


# Create your views here.
def register_user(request):
    data = json.loads(request.body)
    user_id = data.get('openid')
    user = User.objects.filter(openid=user_id)
    if not user:
        address = data.get('country') + ' ' + data.get('province') + ' ' + data.get('city')
        user = User(openid=user_id, name=data.get('nickName'), avatar=data.get('avatarUrl'),
                    address=address)
        user.save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False, 'openid': user_id})


def get_dynamics(request):
    page = request.GET.get('page')
    query = Dynamics.objects.all()
    dynamics = list(query)
    if not query:
        return JsonResponse({'status': True, 'data': []})
    dynamics, total_page = get_page(dynamics, page)
    dynamics_list = []
    print(dynamics)
    for item in dynamics:
        dynamic = {}
        pictures = DynamicsPicture.objects.filter(dynamics=item)
        dynamic['user'] = item.user.name
        dynamic['avatar'] = item.user.avatar
        dynamic['time'] = item.time
        dynamic['text'] = item.text
        dynamic['image'] = [picture.img for picture in pictures]
        dynamics_list.append(dynamic)
    return JsonResponse({'data': dynamics_list, 'status': True, 'total_page': total_page})


def add_dynamic(request):
    data = json.loads(request.body)
    user_id = data.get('user_id')
    user = User.objects.filter(openid=user_id)
    if not user:
        return JsonResponse({'status': False, 'error': '未找到用户'})
    else:
        user = user[0]
    dynamic = Dynamics(user=user, text=data.get('text'))
    dynamic.save()
    return JsonResponse({'status': True})
