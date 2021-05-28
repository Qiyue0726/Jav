from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets

# Create your views here.
from fucos.functions.resource import getVideos
from fucos.models import *


def getUser(request):
    #if request.GRT:
        user = {'name': 'zhangsan','age': 24}
        return JsonResponse(user)

def toLogin(request):
    return render(request, 'login.html')

def index1(request):
    user = request.POST.get("user", "")
    pwd = request.POST.get("pwd", '')

    if user and pwd:
        n = info.objects.filter(name = user,pwd = pwd).count()
        if n >= 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("帐号密码错误")
    else:
        return HttpResponse("登录失败")

def index(request):
    videos = getVideos()
    print(videos)
    return render(request,'index.html',{'videos':videos})


