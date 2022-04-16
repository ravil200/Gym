from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            to_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                subject = f'Welcome to our restaurant {name}'
                message = f'Thank you for Contact us {name}\n Your response is been noted \n We will contact you shortly' \
                          f'Okey we are waiting for you {message}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [to_email]
                send_mail(subject, message, email_from, recipient_list)
            except Exception as er:
                return HttpResponse(er)

            return redirect('contact:send_email')
    else:
        form = ContactForm()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def send_success(request):
    return redirect(request, 'index.html')