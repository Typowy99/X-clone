from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    posts = models.ManyToManyField('Post',
        symmetrical=False,
        related_name='author',
        blank=True)
    follows = models.ManyToManyField('self', 
        symmetrical=False, 
        related_name='followed_by',
        blank=True)
    last_activity = models.DateTimeField(auto_now=True)
    #profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    

class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f'Post by: {self.post_author}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'{self.comment_text}'
