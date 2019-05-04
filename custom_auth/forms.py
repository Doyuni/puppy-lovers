from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, LOCATIONS

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    real_name = forms.CharField(required=True, max_length=20)
    phone_number = forms.CharField(required=True, max_length=20)
    age = forms.IntegerField(required=True)
    address1 = forms.CharField(required=True, widget=forms.Select(choices=LOCATIONS))

    class Meta:
        model = CustomUser
        fields = ("email", "real_name", "phone_number", "age", "username", "address1", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        user.real_name = self.cleaned_data["real_name"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.age = self.cleaned_data["age"]
        user.username = self.cleaned_data["username"]
        user.address1 = self.cleaned_data["address1"]

        if commit:
            user.save()
        return user
    
    
class CustomUserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())