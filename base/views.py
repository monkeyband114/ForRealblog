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
    
    
    context = {'post': post, 'tags': tags}
    return render(request, 'base/postpage.html', context)
