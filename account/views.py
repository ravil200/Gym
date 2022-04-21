<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .models import User



def send_user(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                subject = f'Добро пожаловать в наш фитнес-клуб {username}'
                message = f'Спасибо, что связались с нами {username} \n Ваш ответ принят к сведению \n Мы свяжемся с вами в ближайшее время' \
                    
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, email_from, recipient_list, phone)
                print('sended')
                User.objects.create(username=username,
                                            email=email,
                                            phone=phone,
                                            message=message).save()
            except BadHeaderError:
                return HttpResponse('invalid data')
            
        return redirect('/')
    else:
        form = ContactForm()

        context = {
        'form': form
        }
        return render(request, 'blog/index.html', context)
=======
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
>>>>>>> 3628f08731f099a6d2224679f692a994365df98b
