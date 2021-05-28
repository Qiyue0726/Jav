from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets

# Create your views here.
from fucos.functions.resource import getVideos
from fucos.models import *


def index(request):
    videos = getVideos()
    # print(videos)
    showNum = int(SysOptions.objects.get(option_key='showNum').option_value)
    return render(request,'index.html',{'videos':videos,'showNum':showNum})


