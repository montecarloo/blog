
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_view, name='home')
    #path('home/<int:a>', views.blog_view_str, name='home2')
]
