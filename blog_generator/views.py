from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.conf import settings
from pytube import YouTube
import assemblyai as aai
import os
import openai
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
        transcription = get_transciption(yt_link)
        if not transcription:
            return JsonResponse({'error': 'No transcript found'})
        blog = generate_blog_transcription(transcription)
        if not blog:
            return JsonResponse({'error': 'No blog generated'})
       
        return JsonResponse({'content': blog})
        #print(transcript)
    else:
        return JsonResponse({'error': 'Invalid request method'})

    # get yt video title
def get_title_vid(link):
    yt = YouTube(link)
    title = yt.title
    return title

def download_audio(link):
    yt = YouTube(link)
    video = yt.streams.get_audio_only()
    output = video.download(output_path=settings.MEDIA_ROOT)
    base, ext = os.path.splitext(output)
    new_file = base + '.mp3'
    os.rename(output, new_file)
    return new_file
    # get transcript from yt video using assemblyai
def get_transciption(link):
    audio_file = download_audio(link)
    aai.settings.api_key = "6d50304a25eb4cfbaf35c6165f3e09eb"

    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(audio_file)
    return transcript.text

def generate_blog_transcription(transcript):
    openai.api_key = "xxxxxxx"
    prompt = f"Based on the following transcript from a YouTube video, write a comprehensive blog article, write it based on the transcript, but dont make it look like a youtube video, make it look like a proper blog article:\n\n{transcript}\n\nArticle:"
    response = openai.Completion.create(
        model="gpt-3.5-turbo", 
        prompt=prompt, 
        max_tokens=1000)

    generated_blog = response.choices[0].text.strip()
    return generated_blog

  

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


