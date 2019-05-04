from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import login, authenticate, logout


from .forms import CustomUserCreationForm, CustomUserLoginForm
# Create your views here.

@csrf_protect
def register_user(request):    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
                        
            login(request, new_user)
            return redirect('welcome')

    args = {}

    args['form'] = CustomUserCreationForm()

    return render(request, 'custom_auth/registration.html', args)

@csrf_protect
def signin_user(request):
    if str(request.user) is not "AnonymousUser":
        return redirect('welcome')
    
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            return redirect("custom_user_login")
        
    context = {}    
    context['form'] = CustomUserLoginForm()
    
    return render(request, 'custom_auth/signin.html', context)


def signout_user(request):
    if not request.user:
        return HttpResponseRedirect('/')

    logout(request)
    return redirect('welcome')
