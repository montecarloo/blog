
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog_view, name='home'),
    path('<int:id>/', views.post_view, name='post')
    #path('home/<int:a>', views.blog_view_str, name='home2')
]
