from django.shortcuts import render
import django
import json
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse

from user.models import User


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
