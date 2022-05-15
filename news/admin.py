from django.contrib import admin
from .models import Story,Comment


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['by','title','time']
    list_per_page = 10


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['by','time']
    list_per_page = 10