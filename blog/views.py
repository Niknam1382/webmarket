from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.
def blog_home(request) :
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_single(request,pid) :
    post = get_object_or_404(Post, pk=pid, status=True)
    context = {'post': post}
    return render(request, 'blog-single.html', context)

