from django.urls import path
<<<<<<< HEAD
from .views import send_user

app_name = 'account'

urlpatterns = [
    path('send_email', send_user, name='send_user'),
]
=======
from .views import register


urlpatterns = [
    path('register', register, name='register'),
]


>>>>>>> 3628f08731f099a6d2224679f692a994365df98b
