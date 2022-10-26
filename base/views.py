from email.message import Message
import json
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


def ddeleteComment(request):
    data = json.loads(request.body)
    userId = data['userId']
    commentId = data['commentId']
    print('userid:', userId)
    print('commentid:', commentId)
    
    
    comment = CommentChat.objects.get(id=commentId)
    user = User.objects.get(id=userId)
    
    if user != comment.user:
        print('deleted not working')
        return JsonResponse('cannot delete not your message', safe=False)
        
        
        
    if request.method == 'POST':
        comment.delete()
        print('deleted')
    
    return JsonResponse('deleted comment', safe=False)