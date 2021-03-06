from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from posts.forms import PostForm, CommentForm
from posts.models import Post, PostComment


def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts':posts,
        'comment_form':comment_form,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    if not request.user.is_authenticated:
        return redirect('members:login')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post-list')
    form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'posts/post_create.html', context)

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    context = {
        'post':post,
        'comment_form':comment_form,
    }
    return render(request, 'posts/post_detail.html', context)

def comment_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('members:login')

    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            print(request.GET)
            next = request.GET.get('next', '').strip()
            print(next)
            if next:
                return redirect(next)
            return redirect('posts:post-detail', pk=pk)

def post_delete(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        if post.author == request.user:
            post.delete()
            return redirect('posts:post-list')
        else:
            raise PermissionDenied('작성자가 아닙니다.')

def comment_delete(request, pk):
    next_path = request.GET.get('next','').strip()

    if request.method == 'POST':
        comment = get_object_or_404(PostComment, pk=pk)
        if comment.author == request.user:
            comment.delete()
            if next_path:
                return redirect(next_path)
            return redirect('posts:post_detail', pk=comment.post.pk)
        else:
            raise PermissionDenied('작성자가 아닙니다')



