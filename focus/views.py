from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets

# Create your views here.
from focus.functions.actor_init import getActor, increActor
from focus.functions.resource import getVideos
from focus.models import *

javUrl = SysOptions.objects.get(option_key='domain').option_value

def index(request):
    videos = getVideos()
    # print(videos)
    showNum = int(SysOptions.objects.get(option_key='showNum').option_value)
    return render(request,'index.html',{'videos':videos,'showNum':showNum,'javUrl':javUrl})

def actor(request):
    getActor()
    # increActor('S',58)
    return HttpResponse(request)


