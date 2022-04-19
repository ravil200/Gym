from django.urls import path
from blog.views import send_email, send_success


urlpatterns = [
    path('send_email', send_email, name='send_email'),
    path('success/', send_success, name='send_success'),
]