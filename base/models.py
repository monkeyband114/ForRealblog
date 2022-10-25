from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User

class Tags(models.Model):
    name = models.CharField(null=True, blank=True, max_length=30)
    
    def __str__(self):
        return self.name
    
class Images(models.Model):
    image = models.ImageField()
    name = models.ForeignKey('Blogpost', on_delete=models.CASCADE, default="placeholder.png")
    
    def __str__(self):
        return str(self.image)

class CommentChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey('Blogpost', on_delete=models.CASCADE, default='4')
    comment = models.TextField(max_length=100, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
class Blogpost(models.Model):
    title = models.TextField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.TextField(blank=True, null=True)
    tag = models.ManyToManyField(Tags, related_name='tags', blank=True)
    image = models.ImageField(null=True, default="placeholder.png")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
