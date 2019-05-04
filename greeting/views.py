from django.shortcuts import render

# Create your views here.1
def main(request):
    return render(request, 'greeting/main.html')

def welcome(request):
    return render(request, 'greeting/login.html')

def signup(request):
    return render(request, 'custom_auth/registration.html')
 