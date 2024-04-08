from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render
from django.db import transaction
from django.db.models import Q
from django import forms
from main.models import Hobby, Comment, Stories, UserProfile, Statistics
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import requests, openai
from datetime import datetime
import asyncio

from threading import Thread


async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)
        
        for m in chat_msgs[last_idx:]:
            if m[0] != nickname: # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))
        
        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]
        
        last_idx = len(chat_msgs)

@transaction.atomic
def index(request):
    context = {}
    return render(request, 'main/index.html', context)

def meetings(request):
    return render(request, 'main/meetings.html')

def chatgpt_api(prompt):
    openai.api_key =  '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'

    response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=1500,
            stop=None,
            )
    
    return response.choices[0].text.strip()
    
def profileo(request):
    if not request.user.is_authenticated:
        return redirect('loginsystem')
    
    user = request.user
    response = None
    
    try:
        userprofile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        userprofile = None

    if request.method == 'POST':
        content = request.POST.get('content')
        response = chatgpt_api(content)
    
    context = {
        'user': user,
        'response': response,
        'userprofile': userprofile,
    }

    return render(request, 'main/profile-owner.html', context)

def create_story(request):
    hobbies = Hobby.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        hobby_id = request.POST.get('hobby')
        photo = request.FILES.get('photo')

        content = request.POST.get('content')
        try:
            hobby = Hobby.objects.get(pk=hobby_id)
        except Hobby.DoesNotExist:
            return HttpResponse("Hobby does not exist")

        # Check if a story with the same title already exists
        if Stories.objects.filter(title=title).exists():
            return HttpResponse("A story with the same title already exists")

        new_story = Stories(
            title=title,
            content=content,
            hobby=hobby,
            photo=photo,
            user=request.user,
            likes=0  
        )
        new_story.save()

        return redirect('stories')

    return render(request, 'main/create_story.html', {'hobbies': hobbies})

def education(request):
    return render(request, 'main/education.html')

def meetings_working(request):
    return render(request, 'main/meetings_working.html')

def education1(request):
    return render(request, 'main/education1.html')

def education2(request):
    return render(request, 'main/education2.html')
    
def education3(request):
    return render(request, 'main/education3.html')

def stories(request):
    hobbies = Hobby.objects.all()
    stories = Stories.objects.all()
    selected_hobbies_names = request.GET.getlist('Hobby') 
    selected_hobbies_ids = []
    selected_hobbies = []

    if selected_hobbies_names:
        for hobby_name in selected_hobbies_names:
            selected_hobby = get_object_or_404(Hobby, name=hobby_name)
            selected_hobbies_ids.append(selected_hobby.id)
            selected_hobbies.append(selected_hobby)

        stories = Stories.objects.filter(hobby__in=selected_hobbies_ids)
        comment = Comment.objects.all()
        print(stories)
    else:
        comment = Comment.objects.all()
        stories = Stories.objects.all()

    if request.method == 'GET':
        liked_story_title = request.GET.get('like_story')
        if liked_story_title:
            liked_story = get_object_or_404(Stories, title=liked_story_title)
            liked_story.likes += 1
            liked_story.save()
            return redirect("stories")

    return render(request, 'main/stories.html', {'stories': stories, 'hobbies': hobbies, 'selected_hobbies': selected_hobbies, 'comment':comment})

def communities(request):
    hobbies = Hobby.objects.all()
    communities = UserProfile.objects.all()

    selected_hobbies_names = request.GET.getlist('Hobby') 
    selected_hobbies_ids = []
    selected_hobbies = []

    if selected_hobbies_names:
        for hobby_name in selected_hobbies_names:
            selected_hobby = get_object_or_404(Hobby, name=hobby_name)
            selected_hobbies_ids.append(selected_hobby.id)
            selected_hobbies.append(selected_hobby)

        communities = UserProfile.objects.filter(hobby__in=selected_hobbies_ids)
        comment = Comment.objects.all()
    else:
        comment = Comment.objects.all()
        communities = UserProfile.objects.all()

    return render(request, 'main/communities.html', {'communities': communities, 'hobbies': hobbies, 'selected_hobbies': selected_hobbies, 'comment':comment,})

def community_detail(request, community_id):
    hobbies = Hobby.objects.all()
    community = get_object_or_404(UserProfile, id=community_id)
    stories = Stories.objects.filter(user=community.user)
    selected_hobbies_names = request.GET.getlist('Hobby') 
    selected_hobbies_ids = []
    selected_hobbies = []

    if selected_hobbies_names:
        for hobby_name in selected_hobbies_names:
            selected_hobby = get_object_or_404(Hobby, name=hobby_name)
            selected_hobbies_ids.append(selected_hobby.id)
            selected_hobbies.append(selected_hobby)

        # Filter communities based on selected hobbies
        communities = UserProfile.objects.filter(hobby__in=selected_hobbies_ids)
        comment = Comment.objects.all()
    else:
        # Fetch all communities if no hobbies are selected
        communities = UserProfile.objects.filter(id=community_id)
        comment = Comment.objects.all()

    # Pass the community_id to the template context
    context = {
        'community': community,
        'communities':communities,
        'hobbies': hobbies,
        'selected_hobbies': selected_hobbies,
        'stories': stories,
        'comment':comment,
        'community_id': community_id  # Pass the community_id
    }

    return render(request, 'main/community_detail.html', context)

def start_chat_server():
    asyncio.set_event_loop(asyncio.new_event_loop())  # Create a new event loop
    start_server(main, port=8080, cdn=False, debug=True)  # Specify host and port

def chat_detail(request):
    Thread(target=start_chat_server).start()
    return redirect("http://127.0.0.1:8080/")

def story_detail(request, story_id):
    hobbies = Hobby.objects.all()
    story = get_object_or_404(Stories, id=story_id)
    selected_hobbies_names = request.GET.getlist('Hobby') 
    selected_hobbies_ids = []
    selected_hobbies = []

    if selected_hobbies_names:
        for hobby_name in selected_hobbies_names:
            selected_hobby = get_object_or_404(Hobby, name=hobby_name)
            selected_hobbies_ids.append(selected_hobby.id)
            selected_hobbies.append(selected_hobby)

        stories = Stories.objects.all()
        comments = Comment.objects.all()
        print(stories)
    else:
        comments = Comment.objects.all()
        stories = Stories.objects.all()

    if request.method == 'POST':
        content = request.POST.get('content')
        new_comment = Comment(
            date=datetime.now(),
            content=content,
            user=request.user,
            stories=story
            )
        new_comment.save()
        return redirect("story_detail", story_id=story_id)
    
    if request.method == 'GET':        
        liked_story_title = request.GET.get('like_story')
        if liked_story_title:
            liked_story = get_object_or_404(Stories, title=liked_story_title)
            liked_story.likes += 1
            liked_story.save()
            return redirect("story_detail", story_id=story_id)
    
    # Pass the story_id to the template context
    context = {
        'story': story,
        'hobbies': hobbies,
        'comments': comments,
        'selected_hobbies': selected_hobbies,
        'story_id': story_id,
    }
    
    return render(request, 'main/stories_detail.html', context)

def ar(request):
    context = {}
    return render(request, 'main/ar.html', context)

def loginsystem(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('po')
        else:
            return render(request, 'main/loginsystem.html', {'error_message': 'Invalid credentials'})  # Pass an error message

    return render(request, 'main/loginsystem.html')
        
def signupsystem(request):
    hobbies = Hobby.objects.all()
    if request.method == 'POST':
        # Extract form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        hobby_id = request.POST.get('hobby')
        photo = request.FILES.get('photo')
        bio = request.POST.get('bio')

        # Validate passwords
        if password1 != password2:
            return HttpResponse("Passwords do not match")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return HttpResponse("Username is already taken")

        try:
            # Get selected hobby
            hobby = Hobby.objects.get(pk=hobby_id)
        except Hobby.DoesNotExist:
            return HttpResponse("Hobby does not exist")

        # Create User instance
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create UserProfile instance and associate it with User instance
        userprofile = UserProfile.objects.create(
            user=user,
            hobby=hobby,
            photo=photo,
            bio=bio,
        )
        userprofile.save()

        # Authenticate and login user
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('po')
        else:
            return HttpResponse("Failed to authenticate user")

    return render(request, 'main/signupsystem.html', {'hobbies': hobbies, })

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')