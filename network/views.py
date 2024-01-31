from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Comment, Post
from django import forms

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


@login_required(login_url='login')
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_content = form.cleaned_data['comment']
            post = Post.objects.create(post_author=request.user, content=post_content)
            post.save()
            return redirect('index')


def profile_view(request, user_name):
    user_info = User.objects.get(username=user_name)
    posts = Post.objects.filter(post_author=user_info.id).order_by('-created_at')
    return render(request, "network/profile.html", {
        "user_info": user_info,
        "posts": posts
    })



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
