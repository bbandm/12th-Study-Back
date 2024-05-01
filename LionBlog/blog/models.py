from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

    
class HashTag(models.Model):
    hashtag=models.CharField(max_length=100)

    def __str__(self):
        return self.hashtag 
    
class Question(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateTimeField('date published')
    body=models.TextField()
    hashtag=models.ManyToManyField(HashTag)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_buckets', blank=True)
    
    def __str__ (self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
class Comment(models.Model):
    post=models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    username=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at= models.DateTimeField(default=timezone.now)
    
    def approve(self):
        self.save()

    def __str__(self):
        return self.comment_text
