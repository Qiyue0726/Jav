from django.contrib import admin
from django.urls import path

from focus import views
from focus.views import actor

urlpatterns = [
    path('actor/', actor),
]