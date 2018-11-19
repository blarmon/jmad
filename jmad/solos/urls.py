

from django.contrib import admin
from django.urls import path, include
from solos import views

urlpatterns = [
    path('', views.index),
    path('solos/<pk>/', views.SoloDetailView.as_view()),
]
