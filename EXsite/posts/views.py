from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list' : latest_post_list}
    return render(request, 'posts/index.html', context)
    
def post(request):
    return render(request, 'posts/post.html', {})

def getPost(request):
    post = request.POST['post']
    p = Post(Post_text = post, pub_date = timezone.now())
    p.save()
    return HttpResponseRedirect('/posts/')

def display(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/display.html', {'post': post})