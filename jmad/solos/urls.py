

from django.contrib import admin
from django.urls import path, include
from solos import views

urlpatterns = [
    path('', views.index),
    path('recordings/<album>/<track>/<artist>/', views.SoloDetailView.as_view(), name='solo_detail_view'),
]
