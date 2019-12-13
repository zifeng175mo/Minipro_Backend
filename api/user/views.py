from django.shortcuts import render
import django
import json
from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import JsonResponse
from datetime import datetime
from user.util import get_page, judge_allgone

from user.models import User, Dynamics, DynamicsPicture, Comment, Gone, Achievement
from province.models import Province

all_provinces = ['shanxi', 'chongqing', 'sichuan', 'hubei', 'jiangsu', 'hunan', 'jiangxi', 'anhui', 'zhejiang',
                 'guangdong',
                 'guangxi', 'yunnan', 'henan', 'shandong', 'sxi', 'gansu', 'xinjiang', 'neimenggu', 'ningxia',
                 'beijing',
                 'shanghai', 'tianjin', 'heilongjiang', 'jilin', 'liaoning', 'hebei', 'qinghai', 'xizang', 'fujian',
                 'hainan', 'xianggang', 'guizhou', 'taiwan']

achievements = ['小试牛刀', '诗词之王']


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
        for item in all_provinces:
            province = Province.objects.get(name=item)
            Gone(user=user, province=province).save()
        for achievement in achievements:
            Achievement(name=achievement, user=user).save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': True, 'openid': user_id})


def get_dynamics(request):
    page = request.GET.get('page')
    user_id = request.GET.get('id')
    if not user_id:
        query = Dynamics.objects.all()
    else:
        user = User.objects.filter(openid=user_id)
        if user:
            user = user[0]
        query = Dynamics.objects.filter(user=user)
    dynamics = list(query)
    if not query:
        return JsonResponse({'status': True, 'data': []})
    dynamics, total_page = get_page(dynamics, page)
    dynamics_list = []
    for item in dynamics:
        dynamic = {}
        pictures = DynamicsPicture.objects.filter(dynamics=item)
        comment_count = Comment.objects.filter(dynamics=item).count()
        dynamic['id'] = item.id
        dynamic['user'] = item.user.name
        dynamic['avatar'] = item.user.avatar
        dynamic['time'] = item.time
        dynamic['text'] = item.text
        dynamic['image'] = [picture.img for picture in pictures]
        dynamic['like_count'] = item.like
        dynamic['comment_count'] = comment_count
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


def get_comments(request):
    id = request.GET.get('id')
    dynamic = Dynamics.objects.filter(id=id)
    if not dynamic:
        return JsonResponse({'status': False, 'error': '未找到该动态'})
    else:
        dynamic = dynamic[0]
    comments = list(Comment.objects.filter(dynamics=dynamic))
    comments_list = []
    for item in comments:
        comment = {'id': item.id, 'user': item.user.name, 'avatar': item.user.avatar, 'text': item.text,
                   'time': item.time, 'reply': item.reply}
        comments_list.append(comment)
    return JsonResponse({'data': comments_list, 'status': True})


def add_comment(request):
    data = json.loads(request.body)
    if not data:
        return JsonResponse({'status': False, 'error': '数据错误'})
    else:
        user_id = data.get('user')
        user = User.objects.filter(openid=user_id)
        if not user:
            return JsonResponse({'status': False, 'error': '找不到该用户'})
        else:
            user = user[0]
        dynamic_id = data.get('id')
        dynamic = Dynamics.objects.filter(id=dynamic_id)
        if not dynamic:
            return JsonResponse({'status': False, 'error': '找不到该动态'})
        else:
            dynamic = dynamic[0]
        new_comment = Comment(user=user, dynamics=dynamic, reply=data.get('reply'), text=data.get('text'))
        new_comment.save()
        return JsonResponse({'status': True})


def finish_test(request):
    data = json.loads(request.body)
    user_id = data.get('user_id')
    user = User.objects.filter(openid=user_id)
    province_name = data.get('province')
    if not user:
        return JsonResponse({'status': False, 'error': '找不到该用户'})
    else:
        user = user[0]
        province = Province.objects.get(name=province_name)
        gone = Gone.objects.filter(user=user, province=province)
        if not gone:
            return JsonResponse({'status': False, 'error': '查询成就失败'})
        else:
            gone = gone[0]
            gone.gone = True
            gone.save()
            if Gone.objects.filter(user=user, gone=True).count() == 1:
                first_achievement = Achievement.objects.get(user=user, name='小试牛刀')
                first_achievement.achieved = True
                first_achievement.save()
            if judge_allgone(user):
                all_gone_achievement = Achievement.objects.get(user=user, name='诗词之王')
                all_gone_achievement.achieved = True
                all_gone_achievement.save()
            return JsonResponse({'status': True, 'passed': province_name})


def get_gone(request):
    user_id = request.GET.get('user_id')
    user = User.objects.filter(openid=user_id)
    if not user:
        return JsonResponse({'status': False, 'error': '未找到该用户'})
    else:
        user = user[0]
        gone_provinces = Gone.objects.filter(user=user)
        gone_list = []
        for item in gone_provinces:
            if item.gone:
                gone_list.append({
                    'province': item.province.name_ch
                })
        return JsonResponse({'status': True, 'data': gone_list})


def get_achievement(request):
    user_id = request.GET.get('user_id')
    user = User.objects.filter(openid=user_id)
    if not user:
        return JsonResponse({'status': False, 'error': '未找到该用户'})
    else:
        user = user[0]
        all_achievements = Achievement.objects.filter(user=user)
        achievement_list = []
        for achievement in all_achievements:
            achievement_list.append({
                'achievement': achievement.name,
                'achieved': achievement.achieved
            })
        return JsonResponse({'status': True, 'data': achievement_list})
