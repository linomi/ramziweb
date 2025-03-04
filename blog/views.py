from django.shortcuts import render, get_object_or_404

from .models import Post, Tag

# Create your views here.

def landing(request):
    posts = Post.objects.all().order_by("-date")[:4]
    tags = Tag.objects.all()
    return render(request, 'blog/landing.html', {
        'posts': posts,
        'tags': tags
    })

def index(request): 
    posts = Post.objects.all().order_by("-date")
    return render(request,'blog/index.html',{"posts":posts})

def post_detail(request,slug): 
    post = get_object_or_404(Post, slug=slug)
    return render(request,'blog/post_detail.html',{'post':post})
