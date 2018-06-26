from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from posts.forms import PostForm
from posts.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
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
    context = {
        'post':post,
    }
    return render(request, 'posts/post_detail.html', context)