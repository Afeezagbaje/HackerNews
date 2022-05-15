from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Story, Comment


class StoryListView(ListView):
    context_object_name = "stories"
    template_name = "story_list.html"
    model = Story
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Story.objects.filter(title__icontains=query).order_by("-time")[:50]
        
        filter = self.request.GET.get("f")
        if filter:
            return Story.objects.filter(type=filter).order_by("-time")[:50]
        stories = Story.objects.all().order_by("-time")[:50]
        return stories


class StoryDetailView(DetailView):
    context_object_name = "story"
    template_name = "story_detail.html"
    model = Story

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        story = kwargs.get("object", "")
        comments = Comment.objects.filter(parent=story.story_id)
        context["comments"] = comments
        return context
