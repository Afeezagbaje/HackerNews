from celery import shared_task

from utils.api_data import get_stories_data, get_item
from .models import Story, Comment


@shared_task
def get_create_story_comments(id):
    hacker_story = get_item(id)
    story = Story.objects.get(story_id=id)
    comment_ids = hacker_story.get("kids", [])

    for comment_id in comment_ids:
        res = get_item(comment_id)
        comment, _ = Comment.objects.get_or_create(comment_id=comment_id)
        comment.story = story
        comment.comment_id = res.get("id", "")
        comment.type = res.get("type", "")
        comment.by = res.get("by", "")
        comment.time = res.get("time", 0)
        comment.text = res.get("text", "")
        comment.url = res.get("url", "")
        comment.parent = res.get("parent", -1)
        comment.score = res.get("score", 0)

        comment.save()
        
        
@shared_task
def add_stories_db(stories_data):
    for story_data in stories_data:
        story, _ = Story.objects.get_or_create(story_id=story_data["id"])
        story.story_id = story_data.get("id", "")
        story.deleted = story_data.get("deleted", False)
        story.type = story_data.get("type", "")
        story.by = story_data.get("by", "")
        story.time = story_data.get("time", 0)
        story.dead = story_data.get("dead", False)
        story.kids = story_data.get("kids", [])
        story.descendants = story_data.get("descendants", 0)
        story.score = story_data.get("score", 0)
        story.title = story_data.get("title", "")
        story.url = story_data.get("url", "")
        story.is_hackernews = True
        story.save()
        get_create_story_comments(story_data["id"])


@shared_task
def get_stories_interval():
    res = get_stories_data()
    add_stories_db(res)