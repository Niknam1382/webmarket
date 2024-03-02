from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from django.contrib import messages
from blog.forms import CommentForm

# Create your views here.
def blog_home(request, **kwargs) :
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_at__gt=now).order_by('-published_at')
    if kwargs.get('author_username'):
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 4)
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger :
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_single(request,pid) :

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS, 'کامنت شما در صف بررسی قرار گرفت')
        else:
            messages.add_message(request,messages.ERROR, 'کامنت شما ثبت نشد')

    post = get_object_or_404(Post, pk=pid, status=True)
    comments = Comment.objects.filter(post=post.id, approved=True)
    post.counted_views += 1
    post.save()
    context = {'post': post, 'comments': comments}
    return render(request, 'blog-single.html', context)

def blog_category(request, cat_name):
    now = timezone.now()
    posts = Post.objects.filter(status=True, category__name=cat_name).exclude(published_at__gt=now).order_by('-published_at')
    context = {'posts': posts}
    return render(request, 'blog.html', context)

def blog_search(request):
    now = timezone.now()
    posts = Post.objects.filter(status=1).exclude(published_at__gt=now)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts': posts}
    return render(request, 'blog.html', context)