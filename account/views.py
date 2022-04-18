from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        if username:
                user = User.objects.create_user(username=username)
                user.save()
                print('User Created!')
        else:
            print('password not match')
        return redirect('/')
    else:
        return render(request, 'index.html')
