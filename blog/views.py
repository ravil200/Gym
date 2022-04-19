from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message


def home(request):
    return render(request, 'index.html')

def send_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            to_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            Message.objects.create(name=name, email=to_email, message=message)
        
        return redirect('/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'index.html', context)


