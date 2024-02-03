
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    path("add_post", views.add_post, name="add_post"),
    path("profile/<str:user_name>", views.profile_view, name="profile"),
    path("following", views.view_following_posts, name="following"),

    # API Routes
    path("follow/", views.follow, name="follow"),
    path("edit_post/", views.edit_post, name="edit_post"),
    path("like_post/", views.like_post, name="like_post"),
]
