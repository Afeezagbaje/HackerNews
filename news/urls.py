from django.urls import path
from .views import StoryListView, StoryDetailView

app_name = 'news'
urlpatterns = [
    path('', StoryListView.as_view(), name='story-list'),
    path("<str:pk>/", StoryDetailView.as_view(), name="story-detail"),
]