from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        user = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=user, password=passwd)
        if user is None:
            return HttpResponse("failed")
        else:
            login(request, user)
            return HttpResponse(request.user)