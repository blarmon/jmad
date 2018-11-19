

from django.contrib import admin
from django.urls import path, include
from solos import views

urlpatterns = [
    path('', views.index),
    path('solos/<int:pk>/', views.SoloDetailView.as_view()),
]
