from django.contrib import admin
from posts.models import Posts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    lists_display=['title', 'user', 'created_at', 'published', 'category']

