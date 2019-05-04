from django.urls import path

from .views import welcome
from .views import signup
from .views import main

urlpatterns = [
    path('', welcome, name='welcome'),
    path('main/', main, name='main'),
    path('signup/', signup, name='signup'),
]