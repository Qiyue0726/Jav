from django.contrib import admin
from django.urls import path

from focus.views import actor, transferList, addActor, delActor

urlpatterns = [
    path('actor/', actor),
    path('transferList/', transferList),
    path('addActor', addActor),
    path('delActor', delActor),
]