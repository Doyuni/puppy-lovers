from django.urls import path
from .views import (PetTransactionCreateView, PetSupplyTransactionCreateView)
                     
urlpatterns = [
#    path('sales/pet', )
    path('pets/new', PetTransactionCreateView.as_view(), name="pet_transactions_create"),
    path('pet_supplies/new', PetSupplyTransactionCreateView.as_view(), name="pet_supply_transactions_create"),
]