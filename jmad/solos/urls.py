

from django.contrib import admin
from django.urls import path, include
from solos import views

urlpatterns = [
    path('', views.index),
]
