from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def all_blogs(request):
    return render(request, 'all-blogs.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def user_login(request):
    return render(request, 'login.html')

def user_logout(request):
    return render(request, 'login.html')

def user_signup(request):
    return render(request, 'signup.html')


