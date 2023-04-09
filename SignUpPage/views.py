from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib import messages
from .models import Index

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        state = request.POST['state']
        pincode = request.POST['pincode']
    
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect('signup')

        myUser = User.objects.create_user(username, email, password1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()
        messages.success(request, 'Your Account has been Successfully Created!')
        return redirect('index')
    return render(request, 'signup.html')
    
def login(request):
     if request.method == 'POST':
        loginUsername = request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']

        user=authenticate(username=loginUsername,password=loginPassword)

        if user is not None:
            auth_login(request,user)
            messages.success(request, 'You have been Successfully Logged In!')
            return redirect('index')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('signup')
        
     return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('login')

