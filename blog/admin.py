from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug' : ('title',), 'excerpt' : ('content',)}
    list_filter = ('approved', 'created_on', 'category')
    list_display = ('title', 'slug', 'approved', 'created_on', 'category')
    search_fields = ['title', 'content', 'author', 'category']
    summernote_fields = ('content')
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        queryset.update(approved=1)

@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('post','created_on')
    search_fields = ['name', 'email', 'body']