from django.urls import URLPattern, path
from .views import home, send_message



urlpatterns = [
    path('', home, name='home'),
    path('send_message', send_message, name='send_message'),
]