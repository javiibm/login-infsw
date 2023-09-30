from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import admin
from django.http import HttpResponse
# Create your views here.

def login_user(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admin/')
        # Redirect to a success page.
            else:
                messages.error(request, "No está en la base de datos")
        # Return an 'invalid login' error message.
        return render(request, 'core/login.html', {})