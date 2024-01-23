# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:05:17 2024

@author: p1516551
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]