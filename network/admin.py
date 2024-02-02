from django.contrib import admin
from .models import Comment, Post, User

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "follows"]

admin.site.register(User, UserAdmin)
admin.site.register(Comment)
admin.site.register(Post)