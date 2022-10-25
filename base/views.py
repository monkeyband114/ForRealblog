from email.message import Message
from multiprocessing import context
from django.shortcuts import redirect, render
from . models import *
from django.http import HttpResponse, JsonResponse



def homePage(request):
    posts = Blogpost.objects.all()
    context = {'posts': posts}
    
    return render(request, 'base/home.html', context)



def postPage(request, pk):
    post = Blogpost.objects.get(id=pk)
    tags = post.tag.all()
    
    post_comment = post.commentchat_set.all().order_by('-created')
    
    if request.method == 'POST':
        comment = CommentChat.objects.create(
            user = request.user,
            post = post,
            comment=request.POST.get('body')
        )
    
    context = {'post': post, 'tags': tags, 'post_comment':post_comment}
    return render(request, 'base/postpage.html', context)


def deleteMessage(request, pk):
    
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
        return HttpResponse('cannot delete not your message')
    
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    
    return JsonResponse('deleted comment', safe=False)