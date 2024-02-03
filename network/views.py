from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import User, Comment, Post
from django import forms
import json

class PostForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-label', 'rows': '3', 'style': 'width: 100%;'}), label=False)


def index(request):
    posts = Post.objects.all().order_by('-created_at')
    if request.user.is_authenticated:
        form = PostForm()
        return render(request, "network/index.html", {
            "form": form,
            "posts": posts
        })
    return render(request, "network/index.html")


def all_users(request):
    if request.user.is_authenticated:
        users = User.objects.exclude(id=request.user.id)
        return render(request, "network/all_users.html", {
            "users": users
        })
    else:
        users = User.objects.all()
        return render(request, "network/all_users.html", { "users": users })



@login_required(login_url='login')
def view_following_posts(request):
    users_followed = request.user.follows.all()
    posts = Post.objects.filter(post_author__in=users_followed).order_by('-created_at')
    return render(request, "network/following.html", {"posts": posts})


@login_required(login_url='login')
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_content = form.cleaned_data['comment']
            post = Post.objects.create(post_author=request.user, content=post_content)
            post.save()
            return redirect('index')


@csrf_exempt
@login_required(login_url='login')
def edit_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post_new_content = data.get('post_content')

        if post_id and post_new_content:
            post_to_update = get_object_or_404(Post, id=post_id)

            #check user is author post
            if request.user == post_to_update.post_author:
                post_to_update.content = post_new_content
                post_to_update.save()
                return JsonResponse({'message': 'Post updated successfully.'})
            else:
                return JsonResponse({'error': 'You are not authorized to edit this post.'}, status=403)
        else:
            return JsonResponse({'error': 'Missing post_id or post_content'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)


@csrf_exempt
@login_required(login_url='login')
def like_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        post_id = data.get('post_id')
        post = get_object_or_404(Post, id=post_id)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            return JsonResponse({'like': False, 'likes_count': post.likes.count()})
        else:
            post.likes.add(request.user)
            return JsonResponse({'like': True, 'likes_count': post.likes.count()})

    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)  


def profile_view(request, user_name):
    profile = User.objects.get(username=user_name)
    posts = Post.objects.filter(post_author=profile.id).order_by('-created_at')
    return render(request, "network/profile.html", {
        "profile": profile,
        "posts": posts,
    })


@csrf_exempt
@login_required(login_url='login')
def follow(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        if username:
            user_to_follow = get_object_or_404(User, username=username)
            if request.user.follows.filter(id=user_to_follow.id).exists():
                request.user.follows.remove(user_to_follow)
                return JsonResponse({'follow': False})
            else:
                request.user.follows.add(user_to_follow)
                return JsonResponse({'follow': True})
        else:
            return JsonResponse({'error': 'Invalid data'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
    

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
