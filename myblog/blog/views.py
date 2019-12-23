from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.


def blog_view(request):
    querySet = BlogPost.objects.all()

    return render(request, 'posts.html', context={'posts': querySet})


def post_view(request, id):
    querySet = BlogPost.objects.filter(id=id)

    return render(request, 'postview.html', context={'post': querySet[0]})


