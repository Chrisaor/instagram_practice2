from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

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
    form = SignupForm()
    context = {
        'form':form,
    }
    return render(request, 'members/signup.html', context)