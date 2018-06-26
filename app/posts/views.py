from django.http import HttpResponse
from django.shortcuts import render

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
        else:
            return HttpResponse('Form invalid!')
    else:
        return render(request, 'posts/post_create.html')
