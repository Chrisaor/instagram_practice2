from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    photo = request.FILES.get('photo')
    if request.method == 'POST' and photo:
        photo = request.FILES['photo']
        post = Post.objects.create(photo=photo)
        return HttpResponse(f'<img src="{post.photo.url}">')
    else:
        return render(request, 'posts/post_create.html')

