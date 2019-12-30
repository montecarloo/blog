from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'logout':
            logout(request)
            return HttpResponse('successfully logged out')
        user = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=user, password=passwd)
        if user is None:
            return HttpResponse("wrong username or password")
        else:
            login(request, user)
            return HttpResponse(request.user)