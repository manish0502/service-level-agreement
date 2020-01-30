from django.urls import path
from user.views import register, loginview

urlpatterns = [
    path('register/', register, name='register'),
    path('', loginview, name='loginview'),
]
