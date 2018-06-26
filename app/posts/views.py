from django.shortcuts import render

from posts.models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/post_list.html', context)

def post_create(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        return render(request, 'posts/post_create.html')
    return render(request, 'posts/post_create.html')

