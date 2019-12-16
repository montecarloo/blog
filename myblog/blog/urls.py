
from django.contrib import admin
from django.urls import path

from .views import blog_view

urlpatterns = [
    path('home/', blog_view, name='home')
]
