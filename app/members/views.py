from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.forms import SignupForm

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']


            if User.objects.filter(username=username).exists():
                return HttpResponse(f'Username {username} is already exist!')
            user = User.objects.create_user(
                username=username,
                password=password,
            )
            return HttpResponse(f'{user.username}, {user.password}')
        print(form.cleaned_data)
        print(form.errors)
    else:
        form = SignupForm()
    context = {
        'form':form,
    }
    return render(request, 'members/signup.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect('post-list')
        else:
            return HttpResponse('Login credentials invalid')
    else:
        return render(request, 'members/login.html')
