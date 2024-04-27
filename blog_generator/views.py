from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'index.html')

def all_blogs(request):
    return render(request, 'all-blogs.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('User logged in')
            return redirect('/')
        else:
            error_message = 'Invalid Credentials'
            return render(request, 'login.html', {'error': error_message})
    return render(request, 'login.html')

def user_logout(request):
    return render(request, 'login.html')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeat_password = request.POST['password']
        if password == repeat_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Password does not match'
            return render(request, 'signup.html', {'error': error_message})
    return render(request, 'signup.html')


