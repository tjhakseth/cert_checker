from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse("Success")
        else:
           messages.error(request, "Error")
    else:
       messages.error(request, "Error")

def logout_view(request):
    logout(request)