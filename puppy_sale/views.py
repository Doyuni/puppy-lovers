from django.shortcuts import render

from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from django.contrib.contenttypes.models import ContentType

from .models import Transaction, Pet, PetSupply, TransactionRequest
# Create your views here.

class PetTransactionListView(ListView):
    model = Transaction
    paginate_by = 20
    context_object_name = 'pet_list'
    template_name = "puppy_sale/pet_transaction.html"
    
    queryset = Transaction.objects.filter(transactable_type__model='Pet')

class PetSupplyTransactionListView(ListView):
    model = Transaction
    paginate_by = 20
    template_name = "puppy_sale/pet_supply_transaction.html"
    context_object_name = 'pet_supply_list'
    
    queryset = Transaction.objects.filter(transactable_type__model='PetSupply')

    
class PetTransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "puppy_sale/pet_transaction_create.html"
    success_url = '/sales/pets'
    
    fields = ['transactable_id', 'transactable_name', 'price', 'deadline', 'description']
        
    
    def get_form(self, *args, **kwargs):
        form = super(PetTransactionCreateView, self).get_form(*args, **kwargs)
        form.fields['transactable_id'] = \
            forms.ChoiceField(choices=[
                (pet.pk, pet.name) for pet in Pet.objects.filter(owner=self.request.user)])
        form.fields['transactable_name'].widget = forms.HiddenInput()

        return form
    
    def form_valid(self, form):
        form.instance.transactable_type = ContentType.objects.get_for_model(Pet)
        
        form.instance.owner = self.request.user
        form.instance.owner_name = self.request.user.real_name
        form.instance.owner_address = self.request.user.address1
        
        return super().form_valid(form)
    

class PetSupplyTransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    template_name = "puppy_sale/pet_supply_transaction_create.html"
    success_url = '/sales/pet_supplies'
    
    fields = ['transactable_id', 'transactable_name', 'price', 'deadline', 'description']
        
    
    def get_form(self, *args, **kwargs):
        form = super(PetSupplyTransactionCreateView, self).get_form(*args, **kwargs)
        form.fields['transactable_id'] = \
            forms.ChoiceField(choices=[
                (pet_supply.pk, pet_supply.name) for pet_supply in PetSupply.objects.all()])
        form.fields['transactable_name'].widget = forms.HiddenInput()

        return form
    
    def form_valid(self, form):
        form.instance.transactable_type = ContentType.objects.get_for_model(PetSupply)
        
        form.instance.owner = self.request.user
        form.instance.owner_name = self.request.user.real_name
        form.instance.owner_address = self.request.user.address1
        
        return super().form_valid(form)
    
class TransactionRequestListView(ListView):
    model = TransactionRequest
    paginate_by = 10
    
class PetDetailView(object):
    pass 

class PetSupplyDetailView(object):
    pass

