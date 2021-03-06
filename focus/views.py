import json

from django.core import serializers
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets

# Create your views here.
from focus.functions.actor_init import getActor, increActor, flash
from focus.functions.resource import getVideos
from focus.models import *

javUrl = SysOptions.objects.get(option_key='domain').option_value

def index(request):
    stars = list(FocusActor.objects.values().all().order_by("sort_no"))
    # 第一次打开
    if request.GET.get('page') is None:
        res = getVideos(stars, 1)
        videos = res.get('videoList')
        pageNum = res.get('pageNum')
        showNum = int(SysOptions.objects.get(option_key='showNum').option_value)
        focusList = list()
        for star in stars:
            focusList.append(
                {
                    'actorId':star.get('actor_id'),
                    'actorName': star.get('name')
                }
            )
        return render(request,'index.html',{'videos':videos,'showNum':showNum,'javUrl':javUrl, 'pageNum': pageNum, 'focusList': focusList})
    else:
        videos = getVideos(stars,request.GET.get('page')).get('videoList')
        showNum = int(SysOptions.objects.get(option_key='showNum').option_value)
        return render(request,'box.html',{'videos':videos,'showNum':showNum,'javUrl':javUrl})


def actor(request):
    getActor()
    # increActor('S',58)
    return HttpResponse(request)


def transferList(request):
    actors = []
    count = 0
    pageNum = 0
    page=None
    if request.GET.get('star') is not None and request.GET.get('star') != '':
        searchResult = list(Actor.objects.values().filter(actor_name__icontains=request.GET.get('star')))
        # 每页多少行
        page = Paginator(searchResult, request.GET.get('pageSize'))

    else:
        # actors = list(Actor.objects.values().filter(actor_id__icontains='ayua'))
        allActor = list(Actor.objects.values().all())
        # 每页多少行
        page = Paginator(allActor, request.GET.get('pageSize'))

    actors = page.page(request.GET.get('pageNo')).object_list
    focusActors = list(FocusActor.objects.values_list('actor_id',flat=True))
    # 总数量
    count = page.count
    # 总页数
    pageNum = page.num_pages
    return JsonResponse({'actors':actors, 'focusActors':focusActors, 'count':count, 'pageNum':pageNum})

def addActor(request):
    if request.method == 'POST':
        try:
            actors = json.loads(json.loads(request.body.decode('utf-8')).get('actors'))
            starts = []
            index = FocusActor.objects.count()
            for i,actor in enumerate(actors):
                starts.append(FocusActor(actor_id=actor.get('value'),name=actor.get('title'),sort_no=index + i + 1))
            FocusActor.objects.bulk_create(starts)
            return JsonResponse({'msg':'关注成功','status':1})
        except:
            return JsonResponse({'msg':'关注失败','status':0})
    else:
        return JsonResponse({'msg':'请使用POST请求'})

def delActor(request):
    if request.method == 'POST':
        try:
            actors = json.loads(json.loads(request.body.decode('utf-8')).get('actors'))
            for actor in actors:
                FocusActor.objects.filter(actor_id=actor.get('value'),name=actor.get('title')).delete()
            return JsonResponse({'msg':'取消关注成功', 'status':1})
        except:
            return JsonResponse({'msg':'取消关注失败', 'status':0})
    else:
        return JsonResponse({'msg':'请使用POST请求'})

def flashActorList(request):
    if request.method == 'POST': 
        try:
            flash()
            return JsonResponse({'msg':'更新成功','status':0})
        except:
            return JsonResponse({'msg':'更新失败','status':0})
    else:
        return JsonResponse({'msg':'请使用POST请求'})