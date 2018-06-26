from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username and password:
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            return HttpResponse(f'{user.username}, {user.password}')
    return render(request, 'members/signup.html')