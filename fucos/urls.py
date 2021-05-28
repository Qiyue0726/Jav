from django.contrib import admin
from django.urls import path

from fucos import views

urlpatterns = [
    path('toLogin', views.toLogin),
    path('index', views.index),
    path('getUser',views.getUser)
]