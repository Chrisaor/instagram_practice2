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
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post.objects.create(
                photo=form.cleaned_data['photo']
            )
            return HttpResponse(f'<img src="{post.photo.url}">')
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
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            PostComment.objects.create(
                post=post,
                content=form.cleaned_data['content']
            )
            print(request.GET)
            next = request.GET.get('next')
            print(next)
            if next:
                return redirect(next)
            return redirect('posts:post-detail', pk=pk)
