# Register your models here.
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


# Register your models here.py
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    form = CustomUserCreationForm
    list_display = ("email", "real_name", "phone_number", "username", "age", "address1", "is_staff", "is_active")
    list_filter = ["is_staff", "is_active"]

    fieldsets =  (
        (None, {
            'classes': ('wide',),
            'fields': ("email", "real_name", "username", "age", "phone_number", "address1", "groups", "is_active", "is_staff", "password1", "password2")
        }),
    )
