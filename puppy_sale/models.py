from django.conf import settings 
from django.db import models

from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
    
class Transaction(models.Model):
    """
    class Transaction
    
    사용자 간의 거래를 나타내는 모델    
    ## 
    
    ## 거래 정보
    * transactable_type : 거래의 종류를 나타내는 정보
    * transactable_object : 무엇을 거래하는지 나타내는 정보
    * price : 거래 가격
    * completed : 거래 완료 여부    
    * deadline : 언제까지 거래할 것인지 정보
    
    ## 거래의 세부 정보
    * description
    
    """    
    transactable_id = models.PositiveIntegerField(default=1)
    transactable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    transactable_name = models.CharField(max_length=30, default="")
    transactable = GenericForeignKey('transactable_type', 'transactable_id') 
    price = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)    
    deadline = models.DateField(blank=False, null=False)
         
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=30, default="yourname")
    owner_address = models.CharField(max_length=2, blank=False, null=False)
    
    description = models.TextField(blank=False, null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class TransactionRequest(models.Model):
    """
    class TransactionRequest
    거래(Transaction) 요청을 나타내는 모델
    """
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    requester_name = models.CharField(max_length=30, blank=False, null=False)
    
    comment = models.TextField(blank=False, null=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    
# Create your models here.
class Pet(models.Model):
    """
    class Pet
    반려동물의 정보를 나타내는 모델
    * name  : 반려동물의 이름
    * breed : 반려동물의 품종
    * birth_date : 반려동물의 생년월일
    * owner : 반려동물의 소유주
    * owner_name : 반려동물 소유주 이름
    * personality : 반려동물의 성격
    """
    name  = models.CharField(max_length=30, blank=False, null=False)
    breed = models.CharField(max_length=30, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    owner_name = models.CharField(max_length=30, default="yourname")
    personality = models.CharField(max_length=20, blank=False)
    transactions = GenericRelation(Transaction)

    
class PetSupply(models.Model):
    """ 
    class PetSupply    
    애완용품을 나타내는 정보
    
    """
    name = models.CharField(max_length=30, blank=False, null=False)
    description  = models.TextField(blank=False, null=False)
    transactions = GenericRelation(Transaction)
    
    class Meta:
        db_table = "pet_supplies"