from multiprocessing import context
from django.shortcuts import render
from . models import *



def homePage(request):
    posts = Blogpost.objects.all()
    context = {'posts': posts}
    
    return render(request, 'base/home.html', context)



def postPage(request, pk):
    post = Blogpost.objects.get(id=pk)
    tags = post.tag.all()
    image = post.image
    
    
    context = {'post': post, 'tags': tags, 'image':image}
    return render(request, 'base/postpage.html', context)
