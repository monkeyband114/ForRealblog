from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)
    
    def __str__(self):
        return self.name

class Blogpost(models.Model):
    title = models.TextField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(Tags, related_name='tags', blank=True)
    
    
    def __str__(self):
        return self.title
