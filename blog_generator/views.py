from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from pytube import YouTube
import assemblyai as aai

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'index.html')

@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        yt_link = data['link']
        get_title_vid(yt_link)
       
        return JsonResponse({'content': get_title_vid})
        print(transcript)
    else:
        return JsonResponse({'error': 'Invalid request method'})

    # get yt video title
def get_title_vid(link):
    yt = YouTube(link)
    yt_title = yt.yt_title
    return title

def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.get_audio_only()
    output = video.download(output_path=settings.MEDIA_ROOT)
    # get transcript from yt video using assemblyai
def get_transciption(link):
    pass
  

    # use open ai to generate blog

    # save blog to database

    # return article as a response


def all_blogs(request):
    return render(request, 'all-blogs.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            #print('User logged in')
            return redirect('/')
            print('User logged in')
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


