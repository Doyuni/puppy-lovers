from django.urls import path
from .views import register_user, signin_user, signout_user

urlpatterns = [
    path('signup', register_user, name='signup'),
    path('signin', signin_user, name='login'),
    path('signout', signout_user, name='logout')
]