from django.contrib import admin
from django.db import models
from .models import Comment,Contribution

@admin.register(Contribution)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title','author','faculty','date_posted')
    list_display_links = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','commenter','date_posted')
    list_display_links = ('post',)
