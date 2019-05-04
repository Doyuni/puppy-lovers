from django.contrib import admin
from .models import Pet, PetSupply, Transaction, TransactionRequest

# Register your models here.
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "breed", "owner", "personality")
    
@admin.register(PetSupply)
class PetSupplyAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("transactable_type", "transactable",
                    "price", "completed", "deadline", "description")
   
@admin.register(TransactionRequest)
class TransactionRequestAdmin(admin.ModelAdmin):
    list_display = ("requester_name", "comment")

