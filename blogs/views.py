from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from django.http import Http404

from .models import Blog, Post
from .forms import BlogForm, PostForm

def check_post_owner(request, post):
    if post.owner != request.user:
        raise Http404

def index(request):
    """The home page for blogs"""
    blogs = Blog.objects.order_by('name')
    # reverse sorted so newest posts come first
    posts = Post.objects.order_by('-date_added')
    latest_post = Post.objects.order_by('date_added').first()
    context = {'blogs': blogs, 'posts': posts, 'latest_post': latest_post}
    return render(request, 'blogs/index.html', context)

def post(request, post_id):
    """Show a single post"""
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'blogs/post.html', context)

@login_required
def new_blog(request):
    """Add a new blog category"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = BlogForm()
    else:
        # POST data submitted; process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request):
    """Add a new blog post"""
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = PostForm()
    else:
        # POST data submitted; process data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect('blogs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post"""
    post = Post.objects.get(id=post_id)
    blog = post.blog
    check_post_owner(request, post)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current post
        form = PostForm(instance=post)
    else:
        # POST data submitted; process data
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
