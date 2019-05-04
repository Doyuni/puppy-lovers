from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

SCORES = (
    (0, '☆☆☆☆☆'),
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30, default='') 
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='글 쓴 날짜')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정한 날짜')
    hits = models.IntegerField(default=0, blank=True) 
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('board_detail', args=[self.id])

class Review(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30, default="")
    
    title = models.CharField(max_length=100, blank=False, null=False)
    score = models.IntegerField(choices=SCORES, default=0)
    
    reviewable_id = models.PositiveIntegerField(default=1)
    reviewable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    reviewable_name = models.CharField(max_length=30, default="")
    reviewable = GenericForeignKey('reviewable_type', 'reviewable_id')
    
    description = models.TextField(default='')
    
    def get_absolute_url(self):
        return reverse('review_detail', args=[self.id])
    

class Comment(models.Model):
    commentable_id = models.PositiveIntegerField(default=1)
    commentable_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=30, default="")
    commentable = GenericForeignKey('commentable_type', 'commentable_id')
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    