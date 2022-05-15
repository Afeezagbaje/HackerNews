from time import time
from django.db import models
import datetime
from datetime import timezone
import uuid

dt = datetime.datetime.now(timezone.utc)
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()

class Story(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    story_id = models.PositiveBigIntegerField(unique=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    type = models.CharField(max_length=255)
    by = models.CharField(max_length=255)
    time = models.PositiveBigIntegerField(null=True, default=utc_timestamp)
    dead = models.BooleanField(default=False, blank=True, null=True)
    kids = models.JSONField(default=list, blank=True, null=True)
    descendants = models.PositiveBigIntegerField(null=True)
    score = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    url = models.URLField(null=True)
    is_hackernews = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-time"]
        verbose_name_plural = "Stories"
        
        
        
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_id = models.PositiveBigIntegerField(unique=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=True)
    deleted = models.BooleanField(default=False, blank=True, null=True)
    type = models.CharField(max_length=255)
    by = models.CharField(max_length=255)
    time = models.PositiveBigIntegerField(null=True, default=utc_timestamp)
    dead = models.BooleanField(default=False, blank=True, null=True)
    kids = models.JSONField(default=list, blank=True, null=True)
    parent = models.BigIntegerField(null=True)
    text = models.TextField(null=True)
    
    class Meta:
        ordering = ["time"]
        
    def __str__(self):
        return self.parent.title